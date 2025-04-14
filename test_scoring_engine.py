def test_good_credit():
    from scoring_engine import calculate_risk_score
    info = {'credit_history': 40, 'delinquencies': 0, 'income': 70000}
    score = calculate_risk_score(info)
    assert score > 700

def test_poor_credit():
    from scoring_engine import calculate_risk_score
    info = {'credit_history': 5, 'delinquencies': 5, 'income': 20000}
    score = calculate_risk_score(info)
    assert score < 600