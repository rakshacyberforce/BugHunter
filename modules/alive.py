import os

def check_alive():

    print("[+] Checking Alive Domains")

    os.system("cat results/subdomains.txt | httpx -silent > results/alive.txt")

    print("[✓] Alive domains saved in results/alive.txt")