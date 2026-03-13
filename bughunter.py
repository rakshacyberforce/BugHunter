import os

from modules.banner import banner
from modules.subdomain import find_subdomains
from modules.alive import check_alive
from modules.scan import run_scan

os.makedirs("results", exist_ok=True)

banner()

target = input("Enter Target Domain : ")

print("[1] Starting Subdomain Enumeration")
find_subdomains(target)

print("[2] Checking Alive Domains")
check_alive()

print("[3] Running Vulnerability Scan")
run_scan()

print("Recon Completed")