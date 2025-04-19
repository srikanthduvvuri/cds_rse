from behave import given, when, then
from scoring_engine import calculate_risk_score
import json

@given("an applicant with income {income:d}, credit history {credit_history:d}, and {delinquencies:d} delinquencies")
def step_given_applicant_data(context, income, credit_history, delinquencies):
    context.applicant_info = {
        "income": income,
        "credit_history": credit_history,
        "delinquencies": delinquencies
    }

@when("the risk score is computed")
def step_when_calculate_risk(context):
    context.risk_score = calculate_risk_score(context.applicant_info)

@then("the score should be {expected_score:d}")
def step_then_check_score(context, expected_score):
    assert context.risk_score == expected_score, f"Expected {expected_score}, got {context.risk_score}"

@then("the score should be between {min_score:d} and {max_score:d}")
def step_then_score_between(context, min_score, max_score):
    assert min_score <= context.risk_score <= max_score, f"Score {context.risk_score} not in range {min_score}-{max_score}"
