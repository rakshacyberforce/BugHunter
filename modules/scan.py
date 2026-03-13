import os

def run_scan():

    print("[+] Running Nuclei Vulnerability Scan")

    os.system("""
    nuclei -l results/alive.txt \
    -t zip-backup-files \
    -t wp-user-enum \
    -t wordpress-directory-listing \
    -t phpinfo-files \
    -t generic-env \
    -t package-json \
    -t config \
    -t drupal-jsonapi-user-listing \
    -o results/vulnerabilities.txt
    """)

    print("[✓] Scan finished. Check results/vulnerabilities.txt")