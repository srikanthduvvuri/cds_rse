def calculate_risk_score(applicant_info):
    # Simple mock scoring logic
    credit_history = applicant_info.get('credit_history', 0)
    delinquencies = applicant_info.get('delinquencies', 0)
    income = applicant_info.get('income', 0)
    
    score = 300 + (credit_history * 10) - (delinquencies * 20) + (income // 1000)
    return min(score, 850)