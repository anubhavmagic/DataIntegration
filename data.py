import _mysql
import mmap
#import xlrd
from xlrd import open_workbook,cellname
db = _mysql.connect("localhost", "root", "kaidranzer")
db.query("use countryinfo")
try:
	db.query("DROP TABLE `countryinfo`.`regiondata`;")
	print "gaya"
except:
    print"nahi gaya"
try:   
	db.query("CREATE TABLE `countryinfo`.`regiondata` (  `country` VARCHAR(50) NOT NULL,`region` VARCHAR(50) NOT NULL,  PRIMARY KEY (`country`));")
	print "ghusa"
except:
    print "nahi ghusa"
wb= open_workbook('region.xls')
sheet = wb.sheet_by_index(0)
print "data source opened\n Executing integration operations:\n\n"
print "Selecting relevant data from source and adding to integrated data:\n"

for row_index in range (1,sheet.nrows,9):
	#print "col_index is", col_index
	#print "row_index is", row_index
	contry = sheet.cell(row_index, 6).value
	region = sheet.cell(row_index, 4).value
	#print contry, region
	print int((float(row_index)/sheet.nrows) * 100) , "% completed"
	db.query("INSERT INTO `countryinfo`.`regiondata`(`country`,`region`)VALUES(\""+contry+"\",\""+region+"\");")

	


print "\n\nsource integrated successfuly\n\n"
