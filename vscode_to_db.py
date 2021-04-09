import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "zazaguy5",
    password = "426815",
    database = "warehouse"
)

mycursor = mydb.cursor()
mycursor.execute(
    "select *"
    "from warehouse"
)
result = mycursor.fetchall()
for i in result:
    print(i[3])


