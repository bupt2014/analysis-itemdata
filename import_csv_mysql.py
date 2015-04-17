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

fd=open('tianchi_mobile_recommend_train_user.csv','r')
fd.readline()
csv_data = csv.reader(fd)
#for row in csv_data:
    #print row[3]
    #row[0] = int(round(float(row[0]))) 
    #cursor.execute('INSERT INTO tianchi_mobile_recommend_train_user(user_id,item_id,\
            #behavior_type,user_geohash,item_category,time )' \
          #'VALUES(%s, %s, %s,%s, %s, %s)', row)
cursor.executemany('INSERT INTO tianchi_mobile_recommend_train_user(user_id,item_id,\
            behavior_type,user_geohash,item_category,time )' \
          'VALUES(%s, %s, %s,%s, %s, %s)', 
          csv_data)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
