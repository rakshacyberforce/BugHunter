import os

def find_subdomains(target):

    print("[+] Running Subfinder")

    os.system(f"subfinder -d {target} -silent > results/sub1.txt")

    print("[+] Running Sublist3r")

    os.system(f"sublist3r -d {target} -o results/sub2.txt")

    print("[+] Merging Results")

    os.system("cat results/sub1.txt results/sub2.txt | sort -u > results/subdomains.txt")

    print("[✓] Subdomains saved in results/subdomains.txt")