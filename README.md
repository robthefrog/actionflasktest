## Action Flask Test

### Requirements:
* Python 3
* Flask 0.10 (Or greater)

### Installation
pip3 install flask

### Running
python3 application.py

### Testing
Visit http://localhost:5000

1. /users page will display names with API keys.
2. /\<api_key\>/users will display all of the users in json format given an API key from the / page.
3. /\<api_key\>/\<user_id\>/action_items will display all of the action items owned by a user.
