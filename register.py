import mysql.connector
import json


def register(name, email):
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
    except:
        print("Can't connect to server")
    cursor = mydb.cursor()
    cursor.execute(f"select name from users where email = '{email}'")
    result = cursor.fetchall()
    if result==list():
        cursor.execute(f"insert into users (name, email) values ('{name}', '{email}')")
    else:
        print("you have registered before!")
        exit()

