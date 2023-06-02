# Importing sql connector to connect to my local db
import mysql.connector

# Info needed to connect to db
mydb = mysql.connector.connect(
    host='********',
    user='****',
    password='******',
    port='******',
    database='****'
)

"""initializing cursor in order to execute commands
with MySql"""
mycursor = mydb.cursor()

"""initializing command to populate sql table"""
sql_insert = "INSERT INTO a (b, c) VALUES (%s, %s)"

# This loop prompts user to insert values into the database until
# the loop is broken
looping = True
while looping:
    print("To exit enter 'quit'")
    f = input("value? ")
    if f == 'quit':
        break
    p = input("price? ")
    if p == 'quit':
        break
    sql_print = input("Enter 'Y' to save to DB table: ")
    if sql_print == 'quit':
        break
    elif sql_print == 'Y':
        data = (f, p)
        mycursor.execute(sql_insert, data)
        mydb.commit()
        # Prints the data we enter from the database
        mycursor.execute('SELECT * from a')
        get = mycursor.fetchall()
        for getting in get:
            print(getting)
