#Importing necessary Libraries for making database
import mysql.connector
from mysql.connector import errorcode

#Making database connection
try:
    cnx = mysql.connector.connect(user='user',
                        password='password',
                        host='host',
                        database='db_name')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

#This function asks the user for the database name and returns the connection object
def get_db_connection():
    print("What is the name of your database?")
    db_name = input()
    db = cnx.cursor()
    db.execute("USE " + db_name    )
    return db

def print_all_records():
    db = get_db_connection()
    #List all tables in the db
    db.execute("SHOW TABLES")
    tables = db.fetchall()
    #Loop through all tables in the database
    for t in tables:
        table_name = t[0]
        #print out the table name
        print("\nThis is the "+table_name+" table:")
        #Query all records in the db
        db.execute("SELECT * FROM "+table_name)
        records = db.fetchall()
        #Loop through all records
        for r in records:
            print(r)

#This function searches the database for leaked data
def search_leaked_data():
    print("What term do you want to search for?")
    search_term = input()
    db = get_db_connection()
    #List all tables in the db
    db.execute("SHOW TABLES")
    tables = db.fetchall()
    #Loop through all tables in the database
    for t in tables:
        table_name = t[0]
        #Query the db for matching records
        select_stmt = "SELECT * FROM "+table_name+" WHERE data LIKE '%"+search_term+"%'"
        db.execute(select_stmt)
        records = db.fetchall()
        #Loop through and print all matching records
        print("\nShowing results for "+table_name+": ")
        for r in records:
            print(r)
            
            
  #Contact Development
  def contact():
    print("Whatsapp : +6289518439944")
    print("Telegram : t.me/R3V0LUSIJB3N")

#Main menu
print("Welcome to the Database Leak Finder")
print("Project Dumper Website Database By ./Itingsss")
print("Channel Telegram https://t.me/REVOLUSIJBEN or t.me/REVOLUSIJBEN")
while(True):
    print("")
    print("Choose an option from below:")
    print("1. List All Records")
    print("2. Search for Leaked Data")
    print("3. Contact Development")
    print("4. Exit")
    choice = input()

    if choice == "1":
        print_all_records()
    elif choice == "2":
        search_leaked_data()
    elif choice == "3":
      
    elif choice == "4":
        break
    else:
        print("Not a valid option")