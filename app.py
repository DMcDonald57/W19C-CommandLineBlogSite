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
user_name = input("Please enter your User Name\n")
pass_word = input("Please enter your Password\n")

def login():
    cursor.execute("SELECT id FROM client WHERE username = %s AND password = %s")

login()

