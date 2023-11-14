# Webex Room Management Scripts

![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)

This repository contains scripts to manage memberships in a Webex Room. The scripts read configuration and email data from files, and interact with the Webex API to add or delete members from a specified room.

## Table of Contents

- [Webex Room Management Scripts](#webex-room-management-scripts)
  - [Table of Contents](#table-of-contents)
  - [Files](#files)
  - [Setup](#setup)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
  - [Error Handling](#error-handling)

## Files

1. `add_members.py` - Script to add members to a Webex room.
2. `delete_members.py` - Script to delete members from a Webex room based on a list of emails.
3. `config.ini` - Configuration file containing necessary credentials and room details.
4. `emails.txt` - Example file containing a list of email addresses, one per line.

## Setup
1. Clone this repository.
2. Install the required Python libraries using pip:

```bash
pip install requests
```
```bash
pip install configparser
```

3. Update the `config.ini` file with the appropriate values.

## Configuration

Configure the scripts by updating the `config.ini` file with the appropriate values.

```ini
[general]
email_filename = emails.txt
access_token = your_access_token_here
room_id = your_room_id_here
```
Note: A room ID is equal to a space ID.

## Usage

1. Populate `emails.txt` with the email addresses of the members you want to add or delete from the room.
2. Run the scripts as follows:

```bash
$ python add_members.py
$ python delete_members.py
```

## Dependencies

- Python 3.x
- `requests` library: Install with `pip install requests`
- `configparser` library: Install with `pip install configparser`

## Error Handling

The scripts will output error messages to the console if any issues are encountered, such as invalid credentials, failure to read the email file, or failure to add or delete a member.
