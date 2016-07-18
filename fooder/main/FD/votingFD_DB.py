import sqlite3
import argparse


# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()

ap.add_argument("-ID","--ID",required= True, help = "fooder ID")
ap.add_argument("-RSID","--RSID",required= True, help = "RS ID")
ap.add_argument("-type", "--type", required = True,help = "voting type")
	
args = vars(ap.parse_args())



conn = sqlite3.connect('../DB/foodersDB.db')


# fetch voting number!
cValue=0;

cursor = conn.execute("SELECT *  from "+args['RSID']+" where ID = \""+args['ID']+"\"")
conn.commit()


#update
if( args['type'] == 'gValue'):
	for row in cursor:
		cValue= row[1]+1;
		conn.execute("UPDATE "+args['RSID']+" set goodValue = "+str(cValue)+" where ID= \""+args['ID']+"\"")
		print "{\"ID\":\""+str(row[0])+"\",\"gValue\": "+str(cValue)+",\"bValue\": "+str(row[2])+"}"
else:
	for row in cursor:
		cValue= row[2]+1;
		conn.execute("UPDATE "+args['RSID']+" set badValue = "+str(cValue)+" where ID= \""+args['ID']+"\"")
		print "{\"ID\":\""+str(row[0])+"\",\"gValue\": "+str(row[1])+",\"bValue\": "+str(cValue)+"}"



conn.commit()



conn.close()