from pymongo import MongoClient
import os

client = MongoClient("mongodb://cds-mongodb-1:27017")
db = client.risk_scoring

def save_score(applicant_id, score):
    print(f"Saving score for applicant ID: {applicant_id}, Score: {score}")
    db.scores.insert_one({
        'applicant_id': applicant_id,
        'risk_score': score
    })
    print(f"Score saved for applicant ID: {applicant_id}")