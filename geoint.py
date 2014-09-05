import _mysql
import mmap
#import xlrd
from xlrd import open_workbook,cellname
db = _mysql.connect("localhost", "root", "kaidranzer")
try:
    db.query("DROP DATABASE `countryinfo`;")
except:
    pass
try:
    db.query("CREATE DATABASE countryinfo")
    db.query("USE countryinfo")
    db.query("CREATE TABLE `countryinfo`.`land` (  `country` VARCHAR(50) NOT NULL,  `landarea(sq.km)` INT NULL,  `landboundary(km)` INT NULL,  `totalarea` INT NULL,  PRIMARY KEY (`country`));")
    print "Database has been created \n"
except:
    pass
wb= open_workbook('geo.xls')
sheet = wb.sheet_by_index(0)
print "data source opened\n Executing integration operations:\n\n"
print "Selecting relevant data from source and adding to integrated data:\n"
for row_index in range (5,sheet.nrows):
    contry = sheet.cell(row_index,0).value
    landarea = sheet.cell(row_index,7).value
    if landarea == "NA":
        larea= "NULL"
    else:
        landarea= landarea.split('.')
        landarea = landarea[0]
        larea = ''
        landarea = landarea.split(',')
        for i in range (len(landarea)):
            larea= larea + landarea[i]
        #larea = int(larea)
    landbound = sheet.cell(row_index,8).value
    if landbound == "NA":
        lbound= "NULL"
    else:
        landbound= landbound.split('.')
        landbound = landbound[0]
        lbound = ''
        landbound = landbound.split(',')
        for i in range (len(landbound)):
            lbound = lbound + landbound[i]
        #lbound = int(lbound)
    toalarea = sheet.cell(row_index,13).value
    if toalarea == "NA":
        tarea= "NULL"
    else:
        toalarea= toalarea.split('.')
        toalarea = toalarea[0]
        tarea = ''
        toalarea = toalarea.split(',')
        for i in range (len(toalarea)):
            tarea = tarea + toalarea[i]
        #tarea = int(tarea)
    print int((float(row_index)/sheet.nrows) * 100) , "% completed"
#query here
    try:
        db.query("INSERT INTO `countryinfo`.`land`(`country`,`landarea(sq.km)`,`landboundary(km)`,`totalarea`)VALUES(\""+ contry +"\","+larea+","+ lbound+","+tarea+");")
    except:
        print "Insert Failed"

print "\n\nsource integrated successfuly\n\n"
    
