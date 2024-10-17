import sqlite3
import json

db_path = 'B&B-GE915-17(final).sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM api_feedback")
rows = cursor.fetchall()

columns = [description[0] for description in cursor.description]

api_feedback_data = [dict(zip(columns, row)) for row in rows]

json_path = 'feedbacksdata_final.json'
with open(json_path, 'w') as json_file:
    json.dump(api_feedback_data, json_file, indent=4)

conn.close()

json_path
