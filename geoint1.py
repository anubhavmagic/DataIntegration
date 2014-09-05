import MySQLdb as mdb
import mmap
import unicodedata
import time
#import xlrd
from xlrd import open_workbook,cellname
db = mdb.connect("localhost", "root", "kaidranzer")
db.query("use countryinfo")

files = ['geo1.xls', 'ocean1.xls']
garbage = ['and', 'the', 'of', 'or']

#############Integrating Country database#######

wb= open_workbook('geo1.xls')
sheet = wb.sheet_by_index(0)
cur = db.cursor()
garbage = ['and', 'the', 'of', 'or']
for row_index in range (3, sheet.nrows):
	contry = str(sheet.cell(row_index,0).value)
	larea = str(sheet.cell(row_index, 56).value)
	query = "SELECT * from `countryinfo`.`land` WHERE country = \""+contry+"\""
	cur.execute(query)
	rows = cur.fetchall()

	if not rows:
		words = contry.split(' ')
		for i in range(len(words)):
			words[i] = str(words[i].split(',')[0])
			if words[i] not in garbage:
				query = "SELECT * from land WHERE country like \'%"+words[i]+"%\'"
				cur.execute(query)
				rows = cur.fetchall()
				if not rows:
					for row in rows:
						#print "Query result: ", row[3]
						if row[1] == None:
							print contry
							query = "UPDATE `countryinfo`.`land` SET `landarea(sq.km)` = \""+larea+ "\" WHERE `country` = \""+contry+ "\";"
							cur.execute(query)
	else:
		for row in rows:
			#print "Query result: ", row[3]
			if row[1] == None:
				print contry
				query = "UPDATE `countryinfo`.`land` SET `landarea(sq.km)` = \""+larea+ "\" WHERE `country` = \""+contry+ "\";"
				cur.execute(query)
		#cur.execute(query)
		#rows = cur.fetchall()

	
print "Commiting changes."
db.commit()  # committing changes to the database
cur.close()

#############Integrating Ocean database#######

wb= open_workbook('ocean1.xls')
sheet = wb.sheet_by_index(0)
cur = db.cursor()
for row_index in range (1, sheet.nrows):
	ocean = str(sheet.cell(row_index,0).value)
	print "FIlling data for ocean : ", ocean
	area = str(sheet.cell(row_index, 1).value)
	query = "SELECT * from `countryinfo`.`land` WHERE country = \""+ocean+"\""
	cur.execute(query)
	rows = cur.fetchall()

	if not rows:
		words = contry.split(' ')
		for i in range(len(words)):
			words[i] = str(words[i].split(',')[0])
			if words[i] not in garbage:
				query = "SELECT * from land WHERE country like \'%"+words[i]+"%\'"
				cur.execute(query)
				rows = cur.fetchall()
				if rows:
					for row in rows:
						#print "Query result: ", row[3]
						if row[3] == None:
							query = "UPDATE `countryinfo`.`land` SET `totalarea` = \""+larea+ "\" WHERE `country` = \""+ocean+ "\";"
							cur.execute(query)
	else:
		for row in rows:
			#print "Query result: ", row[3]
			if row[3] == None:
				query = "UPDATE `countryinfo`.`land` SET `totalarea` = \""+area+ "\" WHERE `country` = \""+ocean+ "\";"
				cur.execute(query)
print "making changes"
db.commit()  # committing changes to the database

cur.close()
db.close()
