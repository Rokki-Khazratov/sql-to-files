import json
import pandas as pd

# Load the cleaned JSON data
with open('feedbacksdata_cleaned.json', 'r') as json_file:
    cleaned_feedback_data = json.load(json_file)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(cleaned_feedback_data)

# Save the DataFrame to an Excel file (XLSX format)
xlsx_path = 'feedbacksdata_cleaned.xlsx'
df.to_excel(xlsx_path, index=False)

print(f"Data saved to {xlsx_path}")