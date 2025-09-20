import requests

def check_http_version(target_url):
    try:
        response = requests.get(target_url)
        if 'Server' in response.headers:
            print(f"Server Info: {response.headers['Server']}")
        else:
            print("No Server info found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
