# Forward Assault Account Cracker 🔓
> A high-performance multi-threaded password cracker for Forward Assault
> 
> 🎮 Game: https://www.crazygames.com/game/forward-assault

---

## ✨ Features

* **⚡ Blazing Fast:** Multi-threaded logic for maximum throughput
* **📉 Zero Lag:** Efficient memory management even with 36M+ passwords
* **🏗️ Scalable:** Drop any custom wordlist into the `WorldList` folder
* **🔓 Open Source:** Transparent and community-driven
* **📊 Comprehensive Logging:** Detailed session history in `log.txt`
* **🌍 Multi-Language Support:** Includes wordlists in 12+ languages
* **🎯 Unique Password Filtering:** Automatically removes duplicate passwords across all lists

---

## 📋 Requirements

- Python 3.7+
- `requests` library (for HTTP requests)
- Internet connection (to connect to the FA server)

---

## 🚀 Installation

### Clone the Repository
```bash
https://github.com/DrZushaa/FWD_Password_Cracker.git
cd FWD_Password_Cracker
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Basic Usage
```bash
python main.py
```

### Step-by-Step Guide

1. **Prepare Your Wordlists** (optional)
   - Place `.txt` wordlist files in the `WorldList/` folder
   - Don't have any? No problem! The tool includes 100+ pre-built wordlists 😉

2. **Run the Cracker**
   ```bash
   python main.py
   ```
   - Enter the target username when prompted
   - The tool will load all wordlists and begin cracking

3. **Monitor Progress**
   - Watch real-time output in the terminal
   - Check `log.txt` for detailed session history
   - The cracker will stop as soon as it finds a valid password

---

## ⚙️ How It Works

```
1. Load all .txt files from WorldList/ folder
2. Deduplicate passwords (removes duplicates across all files)
3. Split password list into N chunks (N = WORKERS_NUMBER)
4. Spawn N threads to crack passwords in parallel
5. Each thread hashes passwords with SHA512
6. Send credentials to Forward Assault server
7. Stop on first successful match
8. Log all activity to log.txt
```

### Configuration

Edit these variables in `main.py`:

```python
WORKERS_NUMBER = 2  # Number of concurrent threads (adjust based on CPU cores)
```

---

## 📚 Wordlist Sources

The `WorldList/` folder includes 100+ curated password lists:

### Multi-Language Support
- **German:** Top 1M most common passwords
- **Chinese:** 1M+ common passwords (Simplified & Traditional)
- **Spanish:** Common usernames and passwords
- **French:** Top 20K most common passwords
- **Polish:** Comprehensive password dictionary
- **And 7+ more languages** (Dutch, Italian, Russian, Turkish, etc.)

### Popular Wordlists Included
- `rockyou.txt` - 14M passwords (leaked database)
- `Pwdb_top-10000000.txt` - Top 10M passwords
- `darkweb2017_top-10000.txt` - Dark web breach data
- SCRABBLE dictionaries
- And many more...

📖 **Sources:** See `WorldList/README.md` for detailed attribution

---

## 📝 Output & Logging

### Console Output
```
Username.> targetuser
176 files to load.
Loaded 1000 passwords from rockyou.txt
...
Password found: mypassword123
```

### Log File (`log.txt`)
```
[2026-04-10 15:30] Loaded 1000 passwords from rockyou.txt
[2026-04-10 15:30] Total loaded passwords before filtering: 50000
[2026-04-10 15:30] Unique passwords: 48500
[2026-04-10 15:31] Username: targetuser - Password: mypassword123 [SUCCESS]
```

---

## 🔧 Advanced Usage

### Add Custom Wordlists
1. Place your `.txt` files in the `WorldList/` folder
2. Run the cracker - it will automatically load them

### Adjust Thread Count
Edit `main.py`:
```python
WORKERS_NUMBER = 4  # Use 4 threads instead of 2
```

### Performance Tips
- Increase `WORKERS_NUMBER` for faster cracking (use 2x your CPU cores)
- Use smaller wordlists for faster initial attempts
- Combine most common passwords first for better hit rates

---

## 📊 Performance

- **Memory Usage:** ~500MB-2GB (handles 36M+ passwords)
- **Speed:** 100-500+ attempts/second (depends on server response time)
- **Threads:** Fully parallelized multi-threading
- **Efficiency:** Automatic deduplication across all wordlists

---

## 🔐 Technical Details

- **Hashing Algorithm:** SHA512
- **Payload Format:** 
  ```
  username: [username]
  password: [SHA512_hash]
  ```
- **Target Server:** `https://fa.blayzegames.com/OnlineAccountSystem_NewFPS/`

---

## 📦 Project Structure

```
fwd_passcracker/
├── main.py                    # Main cracker script
├── requirements.txt           # Python dependencies
├── log.txt                    # Session logs (auto-generated)
├── README.md                  # This file
└── WorldList/                 # Wordlist directory (100+ files)
    ├── rockyou.txt
    ├── Pwdb_top-10000000.txt
    └── ... (100+ more wordlists)
```

---

## 📝 Author & Credits

**Author:** looder (iQ)  
**Discord:** 3yni

**Wordlist Credits:**
- Pwdb-Public project
- RockYou leaked database
- Various open-source password collections
- See `WorldList/README.md` for full attribution

---

## ⚖️ Disclaimer

> ⚠️ **LEGAL WARNING**
> 
> This project is provided **for educational and authorized security testing purposes only**.
> 
> - Only use this tool on accounts you own or have explicit permission to test
> - Unauthorized access to computer systems is illegal
> - The developer is not responsible for any misuse or damage caused by this program
> - Use responsibly and ethically
> 
> By using this tool, you agree to use it only for lawful purposes.

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Found a bug or want to improve the cracker? Feel free to:
1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

**Happy cracking! 🔓**
