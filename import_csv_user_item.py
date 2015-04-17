import csv, xlrd, xlwt
import MySQLdb
"""
        select item_id, and get the data into csv
	import useful data from item and user csv
	export distinct_item_category
"""
mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='root',
    db='tianchi')
cursor = mydb.cursor()
fd=open('tianchi_mobile_recommend_train_item.csv','r')
fd.readline()
csv_data = csv.reader(fd)
#print csv_data
text = xlwt.Workbook()
sheet = text.add_sheet('user_item')
csv_data = tuple(csv_data)
t = len(csv_data)
text = xlwt.Workbook()
sheet = text.add_sheet('distinct item_category')
row = 1
cursor.execute("SELECT DISTINCT item_category FROM tianchi_mobile_recommend_train_item")
item_category = cursor.fetchall()
for data in item_category:
    for data1 in data:
        data1 = int( data1)
        sheet.write(row, 0, data1)
        print row
        row = row + 1
text.save('distinct_item_category.xls')
print DONE
