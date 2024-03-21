import mysql.connector

# Replace with your MySQL database credentials
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
database="pgm"
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()
# Example of creating a table
create_table_query = """
CREATE TABLE tenants(
    room_no INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    emailid varchar(50)
)
"""
create_table_query="""
create table New_Joiners(
Name varchar(50),
contact_no int,
room_no int
)
"""
insert_data_query = """
INSERT INTO tenants (room_no,name,age,emailid) VALUES (%s, %s, %s, %s)
"""
data_to_insert1 = (1,"bhavya",23,"bhavya123@gmail.com")
data_to_insert=(2,"geetha",24,"geetha345@gmail.com")
#cursor.execute(insert_data_query,data_to_insert)
#cursor.execute(insert_data_query,data_to_insert1)
select_query="""
select * from tenants
"""
cursor.execute(select_query)
records = cursor.fetchall()
print(records)
db_connection.commit()

