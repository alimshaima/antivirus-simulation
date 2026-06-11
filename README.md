# Basic Antivirus Simulation

## Description
A Python-based antivirus simulation that detects malware using SHA-256 hash matching. Scans files in a specified folder, compares their hashes against a known list of malicious hashes, and quarantines infected files to a "jail" folder.

## Tech Stack
- Python 3.x
- Standard libraries (hashlib, os, shutil)

## How It Works
1. Loads known malicious hashes from `bad_hashes.txt`
2. Calculates SHA-256 hash of each file in target folder
3. Compares hash against malicious list
4. Moves infected files to quarantine (`jail/` folder)

## Installation & Usage

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/antivirus-simulation-python.git

# Navigate to folder
cd antivirus-simulation-python

# Run the antivirus
python antivirus.py
```
### File Structure
antivirus-simulation-python/
├── antivirus.py          # Main scanner
├── bad_hashes.txt        # Known malicious hashes
├── test_folder/          # Folder to scan
│   ├── good_file.txt
│   └── bad_file.txt
└── jail/                 # Quarantine folder (auto-created)

### Sample Output
ANTIVIRUS CHECK BEGINNING...
Good file: good_file.txt
Corrupted file: bad_file.txt
SCAN COMPLETED

### Author
Alima Shaima
