from modules.banner import banner
from modules.subdomain import find_subdomains
from modules.alive import check_alive
from modules.scan import run_scan

banner()

target = input("Enter Target Domain : ")

print("\n[1] Starting Subdomain Enumeration")
find_subdomains(target)

print("\n[2] Checking Alive Domains")
check_alive()

print("\n[3] Running Vulnerability Scan")
run_scan()

print("\nRecon Completed")