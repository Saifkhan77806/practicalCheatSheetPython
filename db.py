import mysql.connector

conn = mysql.connector.connect(password='saif123', user='root')

if(conn.is_connected):
    print("connection established")


mycursor = conn.cursor()

# mycursor.execute("CREATE TABLE khan.person(id int, name varchar(255))")

# mycursor.execute("INSERT INTO khan.person(id, name) VALUES (6, 'aslam')")


mycursor.execute("SELECT * FROM khan.person")

for x in mycursor:
    print(x)