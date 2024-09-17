import requests

def get_pies():
    url = 'https://important.api.endpoint.com/pies'

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
