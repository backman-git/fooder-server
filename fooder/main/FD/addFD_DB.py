import sqlite3
import argparse


# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()

ap.add_argument("-RSID","--RSID",required= True, help = "RS ID")
ap.add_argument("-ID","--ID",required= True, help = "fooder ID")
ap.add_argument("-goodValue", "--gValue", required = True,help = "goodValue of fooder")
ap.add_argument("-badValue", "--bValue", required = True,help = "badValue of fooder")
args = vars(ap.parse_args())





#database
conn = sqlite3.connect('../DB/foodersDB.db')



conn.execute("INSERT INTO "+args["RSID"]+"(ID,goodValue,badValue) \
      VALUES (\""+args['ID']+"\","+args["gValue"]+","+args['bValue']+")");

conn.commit()

print "{\"ID\":\""+args['ID']+"\"}";

conn.close()

