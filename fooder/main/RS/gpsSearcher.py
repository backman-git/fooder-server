import sqlite3



class gpsSearcher:

	def __init__ (self,offset):
		self.conn=sqlite3.connect('../DB/foodersDB.db')
		self.offset=offset



	def search(self,lg,la):

		list =[]
		cursor = self.conn.execute("SELECT ID,latitude,longitude,goodValue,badValue  from RS")

		for row in cursor:
			if(  ((row[1]-self.offset)<= la and la<= (row[1]+self.offset)) and ((row[2]-self.offset)<= lg and lg <= (row[2]+self.offset))    ):
				list.append(row)
   		
		return list


   	def close(self):
		self.conn.close()