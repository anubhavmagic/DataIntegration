import _mysql
import mmap
#import xlrd
from xlrd import open_workbook,cellname
db = _mysql.connect("localhost", "root", "kaidranzer")
db.query("use countryinfo")
try:
    db.query("DROP TABLE `countryinfo`.`populationrateinfo`;")
#    print "pehla theek he"
    db.query("DROP TABLE `countryinfo`.`populationinfo`;")
#    print "doosra theek he"
    db.query("DROP TABLE `countryinfo`.`ageinfo`;")
    print "gaya"
except:
    print"nahi gaya"
    pass
try:
    db.query("CREATE TABLE `countryinfo`.`populationinfo` (  `country` VARCHAR(50) NOT NULL,`(0-14)years` INT NULL,`(15-24)years` INT NULL,`(25-54)years` INT NULL,`(54-64)years` INT NULL, `Above-65 years` INT NULL,  PRIMARY KEY (`country`));")
    db.query("CREATE TABLE `countryinfo`.`populationrateinfo` (  `country` VARCHAR(50) NOT NULL,  `Birth Rate(per 1000 population)` DECIMAL(5,2) NULL, `Death Rate(per 1000 population)`  DECIMAL(5,2) NULL, `Infant Mortality Rate(per 1000 live births)`   DECIMAL(5,2) NULL, `Total Literacy Rate(%)`   DECIMAL(5,2) NULL,  PRIMARY KEY (`country`));")
    db.query("CREATE TABLE `countryinfo`.`ageinfo` (  `country` VARCHAR(50) NOT NULL,  `Median_Age` DECIMAL(5,2) NULL,  `Life_Expectancy_at_birth(years)` DECIMAL(5,2) NULL,  PRIMARY KEY (`country`));")
    print "ghusa"
except:
    print "nahi ghusa"
    pass
wb= open_workbook('pop.xls')
sheet = wb.sheet_by_index(0)
print "data source opened\n Executing integration operations:\n\n"
print "Selecting relevant data from source and adding to integrated data:\n"
contry = ''
b14= ''
fif= ''
twe= ''
khadoos= ''
budhhe= ''
brt= ''
drt=''
imr = ''
le= ''
lr = ''
meda = ''

print"Please wait. Geographic information is being integrated..."
for row_index in range (5,sheet.nrows):
	#print "col_index is", col_index
	#print "row_index is", row_index
	
	contry = sheet.cell(row_index,0).value
	
	below14m = sheet.cell(row_index,1).value
	below14f = sheet.cell(row_index,2).value
#	print "yahan aaya?"
	if below14m == "NA":
			b14m= "NULL"
	else:
			#below14m= below14m.split('.')
			#below14m = below14m[0]
			b14m = ''
			b14f = ''
			below14m = below14m.split(',')
			below14f = below14f.split(',')
			for i in range (len(below14m)):
					b14m= b14m + below14m[i]
			for i in range (len(below14f)):
					b14f= b14f + below14f[i]	
			b14 = int(b14m)+ int(b14f)
#			print "b14m:", b14m, "b14f:", b14f, "b14:", b14

	below14m = sheet.cell(row_index,5).value
	below14f = sheet.cell(row_index,6).value
	if below14m == "NA":
			b14m= "NULL"
	else:
			#below14m= below14m.split('.')
			#below14m = below14m[0]
			fifm = ''
			fiff = ''
			below14m = below14m.split(',')
			below14f = below14f.split(',')
			for i in range (len(below14m)):
					fifm= fifm + below14m[i]
			for i in range (len(below14f)):
					fiff= fiff + below14f[i]	
			fif = int(fifm)+ int(fiff)
#			print "fiff:", fiff, "fifm:", fifm, "fif", fif


	below14m = sheet.cell(row_index,8).value
	below14f = sheet.cell(row_index,9).value
	if below14m == "NA":
			b14m= "NULL"
	else:
			#below14m= below14m.split('.')
			#below14m = below14m[0]
			fifm = ''
			fiff = ''
			below14m = below14m.split(',')
			below14f = below14f.split(',')
			for i in range (len(below14m)):
					fifm= fifm + below14m[i]
			for i in range (len(below14f)):
					fiff= fiff + below14f[i]	
			twe = int(fifm)+ int(fiff)
#			print "fiff:", fiff, "fifm:", fifm, "fif", twe

	below14m = sheet.cell(row_index,11).value
	below14f = sheet.cell(row_index,12).value
	if below14m == "NA":
			b14m= "NULL"
	else:
			#below14m= below14m.split('.')
			#below14m = below14m[0]
			fifm = ''
			fiff = ''
			below14m = below14m.split(',')
			below14f = below14f.split(',')
			for i in range (len(below14m)):
					fifm= fifm + below14m[i]
			for i in range (len(below14f)):
					fiff= fiff + below14f[i]	
			khadoos = int(fifm)+ int(fiff)
#			print "fiff:", fiff, "fifm:", fifm, "fif", khadoos


	below14m = sheet.cell(row_index,13).value
	below14f = sheet.cell(row_index,14).value
	if below14m == "NA":
			b14m= "NULL"
	else:
			#below14m= below14m.split('.')
			#below14m = below14m[0]
			fifm = ''
			fiff = ''
			below14m = below14m.split(',')
			below14f = below14f.split(',')
			for i in range (len(below14m)):
					fifm= fifm + below14m[i]
			for i in range (len(below14f)):
					fiff= fiff + below14f[i]	
			budhhe = int(fifm)+ int(fiff)
#			print "fiff:", fiff, "fifm:", fifm, "fif", budhhe

# Variables for second table start here ---------------------------------------

	rate = sheet.cell(row_index,16).value
	if rate == "NA":
			brt= "NULL"
	else:
			brt = rate
#	print "country",contry,"Birth Rate: ", brt


	rate = sheet.cell(row_index,18).value
	if rate == "NA":
			drt= "NULL"
	else:
			drt = rate
#	print "country",contry,"Dirth Rate: ", drt


	rate = sheet.cell(row_index,33).value
	if rate == "NA":
			imr= "NULL"
	else:
			imr = rate
#	print "country",contry,"infant Birth Rate: ", imr


	rate = sheet.cell(row_index,39).value
	if rate == "NA":
			lr= "NULL"
	else:
			lr = rate
#	print "country",contry,"padhaku rate: ", lr
# Hurrayyy.. teesri tabe shuru
	rate = sheet.cell(row_index,36).value
	if rate == "NA":
			le= "NULL"
	else:
			le = rate
#	print "country",contry,"Life expectancy: ", le

#	print "idhar gya kya?"
	rate = sheet.cell(row_index,43).value
	if rate == "NA":
			meda= "NULL"
		#	print "meda null he bhai"
	else:
			meda = rate
	#print "country",contry,"Median Age: ", meda
	print int((float(row_index)/sheet.nrows) * 100) , "% completed"
#query here
	
	#print "ab to chal kutte"
	try:
		#print "try kiya", col_index
		db.query("INSERT INTO `countryinfo`.`populationinfo`(`country`,`(0-14)years`,`(15-24)years`,`(25-54)years`,`(54-64)years`,`Above-65 years`)VALUES(\""+contry+"\","+str(b14)+","+str(fif)+","+str(twe)+","+str(khadoos)+","+str(budhhe)+");")
		#print "query 1 hui"
		db.query("INSERT INTO `countryinfo`.`populationrateinfo`(`country`,`Birth Rate(per 1000 population)`,`Death Rate(per 1000 population)`,`Infant Mortality Rate(per 1000 live births)`,`Total Literacy Rate(%)`)VALUES(\""+contry+"\","+brt+","+drt+","+imr+","+lr+");")
		#print "query 2 hui"
		db.query("INSERT INTO `countryinfo`.`ageinfo`(`country`,`Median_Age`,`Life_Expectancy_at_birth(years)`)VALUES(\""+contry+"\","+meda+","+le+");")
		#print "query 3 bhi hui"
	except:
		print "Insert failed !"


print "\n\nsource integrated successfuly\n\n"
