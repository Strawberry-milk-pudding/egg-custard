import requests

def get_pies():
    API_KEY = "Secret_1{d0nt_hArdc0de_cr3d5}"
    
    url = 'https://important.api.endpoint.com/pies?key=' + API_KEY

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
