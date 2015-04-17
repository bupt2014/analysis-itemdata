import csv, xlrd, xlwt
import MySQLdb
"""
        select item_id, and get the data into csv
	with import_csv_user_item.py, and should 
	export xls into csv
"""
mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='root',
    db='tianchi')
cursor = mydb.cursor()
fd=open('distinct_item_category.csv')
csv_data = csv.reader(fd)
row = 1
for data in csv_data:
    for data1 in data:
        operation = "INSERT INTO tianchi_mobile_recommend_user_item(user_id, item_id, behavior_type, user_geohash \
            , item_category, time) SELECT user_id, item_id, behavior_type, user_geohash, item_category, time FROM \
            tianchi_mobile_recommend_train_user WHERE item_category = "+ data1  
        cursor.execute(operation)
        print row
	row += 1

cursor.close()
mydb.commit()
mydb.close()
