import hashlib
import itertools
import string

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def brute_force_sha256(target_hash, max_length=4):
    chars = string.ascii_lowercase + string.digits
    
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt_text = ''.join(attempt)
            attempt_hash = sha256_hash(attempt_text)
            
            if attempt_hash == target_hash:
                return attempt_text
    
    return None

if __name__ == "__main__":
    password = "abc1"
    hashed_password = sha256_hash(password)
    print(f"Target Hash: {hashed_password}")
    
    cracked = brute_force_sha256(hashed_password)
    
    if cracked:
        print(f"Password cracked: {cracked}")
    else:
        print("Failed to crack password")
