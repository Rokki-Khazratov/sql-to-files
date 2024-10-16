import sqlite3
import json

db_path = 'GE-users(2 days).sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM api_member")
rows = cursor.fetchall()

columns = [description[0] for description in cursor.description]

api_member_data = [dict(zip(columns, row)) for row in rows]

json_path = 'membersdata_2days.json'
with open(json_path, 'w') as json_file:
    json.dump(api_member_data, json_file, indent=4)

conn.close()

json_path
