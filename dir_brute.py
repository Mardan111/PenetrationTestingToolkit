import requests

def brute_force_dirs(target_url, wordlist):
    with open(wordlist, 'r') as f:
        directories = f.readlines()

    for dir in directories:
        dir = dir.strip()
        url = f"{target_url}/{dir}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Found: {url}")
