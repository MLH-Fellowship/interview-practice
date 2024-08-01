# Python Edition

## Setup
For Linux and Macbook 
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
For Windows 
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
# To run the backend

For macbook/Linux
``` powershell 
python3 manage.py runserver
```

For Windows
``` powershell 
python manage.py runserver
```
## Further Note
If you want to use a custom domain. In track_record/settings.py you can see to the line number 36. Even if you are getting any error related to cors-header 
```
CORS_ALLOWED_ORIGINS = [
      "put your frontend domain link here to get the data"
]

CSRF_TRUSTED_ORIGINS = [
      "put your frontend domain link here to get the data" 
]
```
Add this line in the settings.py file and comment the line no. 32 in settings.py file that not allow any domain to use that particular api


## Adiitional detail
The api is perfectly working and has checked in postman moreover it has good api interface.. if using lets see to it once 🥰
Database here using is db.sqlite.
