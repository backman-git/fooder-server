import sqlite3
import argparse


# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()

ap.add_argument("-ID","--ID",required= True, help = "fooder ID")

ap.add_argument("-longitude", "--long", required = True,help = "longitude of fooder")

ap.add_argument("-latitude", "--lat", required = True,help = "latitude of fooder")	

ap.add_argument("-goodValue", "--gValue", required = True,help = "goodValue of fooder")
ap.add_argument("-badValue", "--bValue", required = True,help = "badValue of fooder")


	
args = vars(ap.parse_args())





#database
conn = sqlite3.connect('../DB/foodersDB.db')


conn.execute('''CREATE TABLE '''+args['ID']+'''
       (
       	ID   varchar(1000) PRIMARY KEY,
       	goodValue INT,
       	badValue INT
       	);''')
		

		
conn.commit()
conn.execute("INSERT INTO RS(ID,latitude,longitude,goodValue,badValue) \
      VALUES ( \""+args['ID']+"\","+args['long']+","+args["lat"]+","+args["gValue"]+","+args['bValue']+")");



conn.commit()
conn.close()

print "{\"ID\": \""+args['ID']+"\"}";



