import sqlite3
import csv


db_path = 'GE-users(2 days).sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM api_member")
rows = cursor.fetchall()

columns = [description[0] for description in cursor.description]

csv_path = 'api_member_data.csv'
with open(csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)

    writer.writerows(rows)  

conn.close()

csv_path
