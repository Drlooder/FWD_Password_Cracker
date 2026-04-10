# Fwd Passcracker 🔒

An advanced tool for password cracking using forward hashing techniques. This tool is designed to assist in security assessments and pentests by evaluating the strength of password hashes.

## Features ✨
- **Fast Hashing**: Utilizes advanced algorithms for quick hash generation.
- **Multi-Platform Support**: Works on Windows, Mac, and Linux.
- **Custom Wordlists**: Load your own wordlists for targeted attacks.
- **Progress Reporting**: Real-time updates on cracking progress.

## Installation 🚀
To install Fwd Passcracker, follow these steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/DrZushaa/fwd_passcracker.git
   cd fwd_passcracker
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 📘
To run Fwd Passcracker, use the following command:
```bash
python fwd_passcracker.py -w <wordlist> -H <hash>
```
Replace `<wordlist>` with the path to your wordlist and `<hash>` with the hash you want to crack.

## Configuration ⚙️
You can customize your experience by modifying the `config.yaml` file in the repository. Parameters you can adjust include:
- **Hash Algorithm**: Specify the hashing algorithm used.
- **Timeout Settings**: Alter the timeout settings for long processes.

## How It Works 🔍
Fwd Passcracker analyzes password hashes and attempts to crack them using a dictionary attack methodology. By iterating through potential passwords from the specified wordlist, it checks against the provided hash until a match is found or the list is exhausted.

## Wordlist Sources 📂
Here are some recommended sources for high-quality wordlists:
- [SecLists](https://github.com/danielmiessler/SecLists)
- [Weakpass](https://weakpass.com/)
- [RockYou](https://github.com/remyk/go-rank/tree/master/rockyou)

## Disclaimer ⚠️
This tool is intended for educational and ethical hacking purposes only. Unauthorized use of this tool against systems you do not own or have explicit permission to test is illegal and unethical. Use responsibly!

---
> **Note**: Always keep your tool updated by checking for the latest releases and updates.
