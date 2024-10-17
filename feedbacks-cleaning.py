import json
from datetime import datetime

# Load the JSON data from the file
with open('feedbacksdata_final.json', 'r') as json_file:
    feedback_data = json.load(json_file)

# Create a dictionary to store the latest feedback for each member_id
latest_feedback = {}

# Loop through all feedback entries
for feedback in feedback_data:
    member_id = feedback['member_id_id']
    created_at = datetime.strptime(feedback['created_at'], '%Y-%m-%d %H:%M:%S.%f')

    # If this is the first entry for the member_id, or if this feedback is newer, update the dictionary
    if member_id not in latest_feedback or created_at > latest_feedback[member_id]['created_at']:
        latest_feedback[member_id] = feedback
        latest_feedback[member_id]['created_at'] = created_at  # Store the datetime object for comparison

# Convert back to list and clean up created_at to string format
cleaned_feedback_data = [
    {**feedback, 'created_at': feedback['created_at'].strftime('%Y-%m-%d %H:%M:%S.%f')}
    for feedback in latest_feedback.values()
]

# Save the cleaned data back to a new JSON file
with open('feedbacksdata_cleaned.json', 'w') as json_file:
    json.dump(cleaned_feedback_data, json_file, indent=4)

print("Cleaned data saved to feedbacksdata_cleaned.json")
