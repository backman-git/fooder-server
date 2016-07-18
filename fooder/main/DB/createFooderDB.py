import sqlite3

conn = sqlite3.connect('foodersDB.db')
print "Opened database successfully";


conn.execute('''CREATE TABLE RS 
       (
       	ID   varchar(1000) PRIMARY KEY,
       	latitude FLOAT,
       	longitude FLOAT,
       	goodValue INT,
       	badValue INT
       	);''');
		

conn.commit()	





print "Table created successfully";

conn.close()