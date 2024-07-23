import mysql.connector
import json


with open("info.json", "r") as js:
    data = js.read()
    data = json.loads(data)

mydb = mysql.connector.connect(
  host= data["server"]["host"],
  user= data["server"]["user"],
  password= data["server"]["password"]
)
