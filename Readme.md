# Example assignment Rest API 
This program also work in brwoser with out add message function.
I recomment to use in Thunder there all the function work.


## Installation & Run
```bash
Clone the Project
# https://github.com/LidorLazar/RestApiMessage
Activesion the ENV 
# \Arba\env\Scripts>activate
Install the requerments
# pip install -r requirements.txt
Run the program 
# py app.py

# API Endpoint : http://127.0.0.1:5000
```
## Example add new message
```bash
{
  "id":1,
  "sender":"test",
  "receiver":"Avi",
  "message":"Hello,World",
  "subject":"program",
  "reading": false ## default is false 
}

```
## 
```
├── ARBA
│   ├── Backend
│       ├── __init__.py  //Initialization program
│       ├── logic.py    // All functions
│       ├── module.py  //Define column in DataBase
│   │──env // This virtual environment folder
│   ├── instance
│   └── API.sqlite3 // Data Base
│
│ 
└── main.py // The file to start the program
```

## API

#### /AllMessage/id
* `GET` : Get all message in specific user


#### /NewMessage
* `POST` : Wirte a new message and append to DB


#### /UnReadMessage/id
* `GET` : Return all the message unread in user

#### /OneMessage/id/index
* `GET` : Return specific message in user

#### /DelMessage/id/index
* `DELETE` : Delete a specific message
