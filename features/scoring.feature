Feature: Risk Scoring
  Scenario: Score high-credit applicant
    Given applicant has good credit history and no delinquencies
    When risk score is calculated
    Then risk score should be high

  Scenario: Score poor-credit applicant
    Given applicant has poor credit history and many delinquencies
    When risk score is calculated
    Then risk score should be low