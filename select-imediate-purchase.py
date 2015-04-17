import csv, xlrd, xlwt
import MySQLdb
"""
	select person who purchase the day after watching;
	未完成，还需修改
"""
mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='root',
    db='tianchi')
cursor = mydb.cursor()
cursor.execute("create table purchase-after-watching( user_id int(12), item_id int(12), behavior_type int(1), user_geohash char(9), item_category int(12), timedatetime);")
cursor.execute("select distinct user_id, item_id from tianchi_mobile_recommend_user_item where behavior_type =4;")
user_data = cursor.fetchall()
for user in user_data:
	cursor.execute("select distinct user_id, item_id, behavior_type, user_goehash, item_category, time from tianchi_mobile_recommend_user_item where user_id = %d and item_id = %d and behavior_type = 4;", user)
	usercursor.fetchall()
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

