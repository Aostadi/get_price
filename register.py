import mysql.connector
import json


try:
    with open("info.json", "r") as js:
        data = js.read()
        data = json.loads(data)

    mydb = mysql.connector.connect(
    host= data["server"]["host"],
    user= data["server"]["user"],
    password= data["server"]["password"],
    database= data["server"]["database"]
    )
    cursor = mydb.cursor()
except:
    print("Can't connect to server")

def register(name, email):
    if check_user_exist():
        print("you have registered before!")
        exit()
    else:
        cursor.execute(f"insert into users (name, email) values ('{name}', '{email}')")

def check_user_exist(email):
    cursor.execute(f"select name from users where email = '{email}'")
    result = cursor.fetchall()
    if result==list():
        return True
    else:
        return False
    

