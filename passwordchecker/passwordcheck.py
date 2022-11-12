import requests
import hashlib
import sys
'''key anonymity'''
def request_password_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_leaked_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if hash_to_check == h:
            return count
    return 0

def passcheck(password):
    sh1pw = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    checksum,tail = sh1pw[:5], sh1pw[5:]
    response = request_password_api(checksum)
    return get_leaked_count(response, tail)

def main(argv):
    for password in argv:
        count = passcheck(password)
        if count:
            print(f'{password} was found {count} times.')
        else:
            print(f'{password} is safe and has not been found')
    return "Done!"

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
