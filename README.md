# Brute Force SHA-256 Password Cracker

## 📌 Overview
This Python script demonstrates a simple brute-force attack to recover a plaintext password from a given SHA-256 hash. The script systematically tries all possible combinations of lowercase letters and digits (0-9) up to a specified length.

## 🚀 How It Works
1. The script hashes a given password using SHA-256.
2. It then attempts to brute-force the hash by generating all possible character combinations.
3. If a match is found, the cracked password is displayed.
4. If no match is found within the defined length, the script returns a failure message.

## 🛠️ Installation & Usage

### Requirements
- Python 3.x
- No external dependencies required

### Running the script
```sh
python brute_force_sha256.py
```

### Expected Output
```
Target Hash: e99a18c428cb38d5f260853678922e03abd8335283be4f57b0193f66a28c1f71
Password cracked: abc1
```

## ⚠️ Disclaimer
This script is for educational purposes only. Do not use it for illegal activities. Always ensure you have permission before attempting security testing.

