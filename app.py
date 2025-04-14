from flask import Flask, request, jsonify
from scoring_engine import calculate_risk_score
from db import save_score

app = Flask(__name__)

@app.route('/risk-score', methods=['POST'])
def risk_score():
    applicant_info = request.json.get('applicant_info', {})
    score = calculate_risk_score(applicant_info)
    save_score(applicant_info.get('applicant_id'), score)
    return jsonify({'risk_score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

