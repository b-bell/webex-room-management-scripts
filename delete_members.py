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


def fetch_memberships(room_id):
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    params = {'roomId': room_id}
    response = requests.get(
        'https://webexapis.com/v1/memberships', headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['items']
    else:
        response.raise_for_status()


def remove_member(membership_id, email):
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.delete(
        f'https://webexapis.com/v1/memberships/{membership_id}', headers=headers)

    if response.status_code == 204:
        print(f'{email} - was successfully deleted from the room.')
    elif response.status_code == 404:
        print(f'{email} - is not a member of this room.')
    else:
        response.raise_for_status()


config = load_config('config.ini')
EMAIL_FILENAME = config['general']['email_filename']
ACCESS_TOKEN = config['general']['access_token']
ROOM_ID = config['general']['room_id']

memberships = fetch_memberships(ROOM_ID)
emails = read_emails(EMAIL_FILENAME)

if emails and memberships:
    for email_line in emails:
        email = email_line.strip('\r\n')
        for membership in memberships:
            if email.lower() == membership["personEmail"].lower():
                try:
                    remove_member(membership["id"], email)
                except requests.exceptions.RequestException as error:
                    print(f'Failed to remove member: {error}')
                    break
else:
    print('No emails provided or memberships found.')
