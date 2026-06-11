import hashlib
import os
import shutil

def load_bad_list():
    with open("bad_hashes.txt", "r") as file:
        bad_hashes = []
        for line in file:
            bad_hashes.append(line.strip())
    return bad_hashes

def get_fingerprint(filename):
    hasher = hashlib.sha256()
    with open(filename, "rb") as f:
        content = f.read()
        hasher.update(content)
    return hasher.hexdigest()

def scan_this_folder(folder_to_scan):
    bad_list = load_bad_list()
    if not os.path.exists("jail"):
        os.makedirs("jail")
    for filename in os.listdir(folder_to_scan):
        full_path = os.path.join(folder_to_scan, filename)
        if os.path.isfile(full_path):
            fingerprint = get_fingerprint(full_path)
            if fingerprint in bad_list:
                print(f"Corrupted file: {filename}")
                shutil.move(full_path, os.path.join("jail", filename))
            else:
                print(f"Good file: {filename}")

print("ANTIVIRUS CHECK BEGINNING...")
scan_this_folder("test_folder")
print("SCAN COMPLETED")
