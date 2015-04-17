#import data from csv to mysql
#import tianchi data train_user data into mysql
#just for tianchi_mobile_recommend_train_user
import csv
import MySQLdb

mydb = MySQLdb.connect(host='127.0.0.1',
    user='root',
    passwd='root',
    db='tianchi')
cursor = mydb.cursor()

fd=open('tianchi_mobile_recommend_train_item.csv','r')
fd.readline()
csv_data = csv.reader(fd)
cursor.executemany('INSERT INTO tianchi_mobile_recommend_train_item( item_id, item_geohash, item_category)' \
          'VALUES(%s, %s, %s)',
          csv_data)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
