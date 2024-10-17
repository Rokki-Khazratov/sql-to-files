import sqlite3
import openpyxl
from openpyxl import Workbook

# Connect to the SQLite database
db_path = 'B&B-GE915-17(final).sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Execute a query to fetch all data from the api_member table
cursor.execute("SELECT * FROM api_member")
rows = cursor.fetchall()

# Get column names
columns = [description[0] for description in cursor.description]

# Create a new Excel workbook and select the active worksheet
xlsx_path = 'fina_membersdata.xlsx'
wb = Workbook()
ws = wb.active
ws.title = "api_member_data"

# Write the column headers
ws.append(columns)

# Write the rows
for row in rows:
    ws.append(row)

# Save the Excel file
wb.save(xlsx_path)

# Close the database connection
conn.close()

# Output the path to the saved Excel file
xlsx_path
