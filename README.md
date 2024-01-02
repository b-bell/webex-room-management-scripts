# webex-room-management-scripts

This repository contains scripts to manage memberships in a Webex Room. The scripts read configuration and email data from files, and interact with the Webex API to add or delete members from a specified room.

![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)

## Table of Contents

- [Webex Room Management Scripts](#webex-room-management-scripts)
  - [Table of Contents](#table-of-contents)
  - [Use Case Description](#use-case-description)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [How to test the software](#how-to-test-the-software)
  - [Known issues](#known-issues)
  - [Getting help](#getting-help)
  - [Author(s)](#authors)
 
## Use Case Description

1. `add_members.py` - Script to add members to a Webex room.
2. `delete_members.py` - Script to delete members from a Webex room based on a list of emails.

## Installation

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
Note: The add_members.py script requires that the user associted with the access token you provided has permissions to add users to the space. Users can only be added to a space if they are a member of your Webex instance. Review [this documentation on the create membership API](https://developer.webex.com/docs/api/v1/memberships/create-a-membership) for more details.

## How to test the software

Start with a small run to ensure you have everything configured correctly. Adding yourself and power users to a room first is always a good way to start. The scripts will output error messages to the console if any issues are encountered, such as invalid credentials, failure to read the email file, or failure to add or delete a member.

## Known issues

There are no known issues at this time.

## Getting help

Please email <iambrianbell@gmail.com>

## Author(s)

This project was written and is maintained by the following individuals:

* Brian Bell <iambrianbell@gmail.com>