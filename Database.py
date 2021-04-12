import mysql.connector

def goods():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "zazaguy5",
        password = "426815",
        database = "warehouse"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "create table if not exists goods(ID char(4), good_name varchar(20) not null, types varchar(15), amount int, primary key (ID));"
        "create table if not exists goodin(ID char(4), date_in varchar(10), amount_in int, primary key (ID), foreign key (ID) references goods(ID));"
        "create table if not exists goodout(ID char(4), date_out varchar(10), amount_out int, primary key (ID), foreign key (ID) references goods(ID));"
    )
    mydb.commit()
    mydb.close()

def add_data(ID, good_name, types, amount):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "zazaguy5",
        password = "426815",
        database = "warehouse"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO goods VALUES(%s, %s, %s, %s)" , (int(ID) ,good_name ,types ,int(amount)))
    mydb.commit()
    mydb.close()

def view_data():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "zazaguy5",
        password = "426815",
        database = "warehouse"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM goods")
    rows = mycursor.fetchall()
    mydb.close()
    return rows

def delete_data(ID):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "zazaguy5",
        password = "426815",
        database = "warehouse"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM goods WHERE ID="+ID)
    mydb.commit()
    mydb.close()

def search_data(ID):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "zazaguy5",
        password = "426815",
        database = "warehouse"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM goods WHERE ID="+ID)
    data1 = mycursor.fetchall()
    mydb.commit()
    mydb.close()
    return data1

def update_data(ID, good_name, types, amount):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "zazaguy5",
        password = "426815",
        database = "warehouse"
    )
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE goods SET ID=%s, good_name=%s, type=%s, amount=%s WHERE ID=%s", (int(ID), good_name, types, int(amount), int(ID)))
    mydb.commit()
    mydb.close()