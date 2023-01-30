import mariadb
import dbcreds

conn = mariadb.connect(
            user=dbcreds.user,
            password=dbcreds.password,
            host=dbcreds.host,
            port=dbcreds.port,
            database=dbcreds.database)

cursor = conn.cursor()

print("Welcome Back.\n")
username = input("Please enter your User Name\n")
password = input("Please enter your Password\n")

def login():
    check = "SELECT id from client WHERE username = %s AND password = %s"
    cursor.execute(check, (username, password))
    results = cursor.fetchone()
    if results is False:
        print("User not found")
    else:
        id = results[0]
        print(id)

login()

