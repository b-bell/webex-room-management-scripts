import configparser
import requests


def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def read_emails(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except Exception as error:
        print(f"Failed to read emails: {error}")


def add_member_to_room(email):
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    data = {'roomId': ROOM_ID, 'personEmail': email}
    response = requests.post(
        'https://webexapis.com/v1/memberships', headers=headers, data=data)

    if response.status_code == 200:
        print(f'{email} - was successfully added to the room.')
    elif response.status_code == 404:
        print(f'{email} - is not a valid Webex email.')
    elif response.status_code == 409:
        print(f'{email} - is already in the room.')
    else:
        response.raise_for_status()


config = load_config('config.ini')
EMAIL_FILENAME = config['general']['email_filename']
ACCESS_TOKEN = config['general']['access_token']
ROOM_ID = config['general']['room_id']

emails = read_emails(EMAIL_FILENAME)

if emails:
    for email_line in emails:
        email = email_line.strip('\r\n')
        try:
            add_member_to_room(email)
        except requests.exceptions.RequestException as error:
            print(f'Failed to add member: {error}')
            break
else:
    print('No emails found in file.')
