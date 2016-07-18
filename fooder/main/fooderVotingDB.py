import sqlite3



import argparse


# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()

ap.add_argument("-ID","--ID",required= True, help = "fooder ID")

ap.add_argument("-type", "--type", required = True,help = "voting type")
	
args = vars(ap.parse_args())



conn = sqlite3.connect('foodersDB.db')


# fetch voting number!
cValue=0;

cursor = conn.execute("SELECT *  from Fooder where ID = "+args['ID'])
conn.commit()


#update
if( args['type'] == 'gValue'):
	for row in cursor:
		cValue= row[3]+1;
		conn.execute("UPDATE Fooder set goodValue = "+str(cValue)+" where ID= "+args['ID'])
		print "{\"ID\":"+str(row[0])+",\"gValue\": "+str(cValue)+",\"bValue\": "+str(row[4])+"}"
else:
	for row in cursor:
		cValue= row[4]+1;
		conn.execute("UPDATE Fooder set badValue = "+str(cValue)+" where ID= "+args['ID'])
		print "{\"ID\":"+str(row[0])+",\"gValue\": "+str(row[3])+",\"bValue\": "+str(cValue)+"}"



conn.commit()



conn.close()