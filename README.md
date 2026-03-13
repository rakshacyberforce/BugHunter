# BugHunter 🐞🔍

BugHunter is a **Bug Bounty Recon Automation Tool** designed to simplify the reconnaissance process during web application security testing.
This tool automates multiple recon steps such as **subdomain discovery, alive host detection, and vulnerability scanning**.

The tool is created for **educational and authorized security testing purposes only.**

---

## Author

**Patel Kunj**
Cyber Security Student
Bug Bounty & Ethical Hacking Enthusiast

---

## Features

* Subdomain Enumeration using multiple tools
* Automatic merge and duplicate removal
* Live host detection
* Vulnerability scanning using Nuclei templates
* Organized result output
* Hacker-style terminal interface

---

## Recon Workflow

Target Domain
↓
Subdomain Enumeration
↓
Merge & Remove Duplicates
↓
Alive Host Detection
↓
Vulnerability Scanning
↓
Save Results

---

## Tools Used

The tool internally uses the following security tools:

* Subfinder – Subdomain enumeration
* Sublist3r – Subdomain discovery
* httpx – HTTP service probing
* Nuclei – Fast vulnerability scanner

---

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/BugHunter.git

Move into the project directory:

cd BugHunter

Run the installation script:

chmod +x install.sh
./install.sh

This will install all required dependencies.

---

## Usage

Run the tool using Python:

python3 bughunter.py

Enter the target domain when prompted.

Example:

Enter Target Domain: example.com

The tool will automatically perform recon and scanning.

---

## Output Files

All results will be saved inside the **results** folder.

results/

subdomains.txt – List of discovered subdomains
alive.txt – Alive domains
vulnerabilities.txt – Vulnerability scan results

---

## Example Output

[phpinfo-files] medium https://example.com/phpinfo.php
[generic-env] high https://api.example.com/.env

---

## Project Structure

BugHunter/

bughunter.py – Main tool file
install.sh – Dependency installer
modules/

subdomain.py – Subdomain discovery
alive.py – Alive host detection
scan.py – Vulnerability scanner
banner.py – Hacker-style interface

results/ – Scan results

---

## Requirements

* Python 3
* Kali Linux or Linux environment
* Git
* Go

---

## Disclaimer

This tool is created for **educational purposes and authorized penetration testing only**.

The developer is not responsible for any misuse of this tool.

Always ensure you have **permission before testing any target**.

---

## Future Improvements

* URL collection
* Parameter discovery
* XSS & SQL injection detection
* Directory brute force
* HTML vulnerability report
* Advanced recon automation

---

## Contributing

Contributions are welcome.

If you want to improve the tool, feel free to fork the repository and submit a pull request.

---

## License

MIT License

---

⭐ If you like this project, consider giving it a star on GitHub.
