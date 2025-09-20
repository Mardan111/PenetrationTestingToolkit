import requests

def scan_http_headers(target_url):
    try:
        response = requests.get(target_url)
        headers = response.headers
        print("HTTP Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")
        for header in ['Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options']:
            if header not in headers:
                print(f"Warning: {header} is missing.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
