import requests
import base64

def get_pies():
    API_KEY = "U2VjcmV0XzJ7ZW5jMGQxbmdfaXNfbm90XzNuY3J5cHQxMG59"
    
    url = 'https://important.api.endpoint.com/pies?key=' + base64.b64decode(API_KEY)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            pies = response.json()
            return pies
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    pies = get_pies()
    print(pies)

if __name__ == '__main__':
    main()
