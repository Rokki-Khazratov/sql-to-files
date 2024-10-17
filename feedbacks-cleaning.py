import json
from datetime import datetime

with open('feedbacksdata_final.json', 'r') as json_file:
    feedback_data = json.load(json_file)

latest_feedback = {}

for feedback in feedback_data:
    member_id = feedback['member_id_id']
    created_at = datetime.strptime(feedback['created_at'], '%Y-%m-%d %H:%M:%S.%f')


    if member_id not in latest_feedback or created_at > latest_feedback[member_id]['created_at']:
        latest_feedback[member_id] = feedback
        latest_feedback[member_id]['created_at'] = created_at 

cleaned_feedback_data = [
    {**feedback, 'created_at': feedback['created_at'].strftime('%Y-%m-%d %H:%M:%S.%f')}
    for feedback in latest_feedback.values()
]

with open('feedbacksdata_cleaned.json', 'w') as json_file:
    json.dump(cleaned_feedback_data, json_file, indent=4)

print("Cleaned data saved to feedbacksdata_cleaned.json")
