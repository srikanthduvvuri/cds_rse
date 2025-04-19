Feature: Risk scoring logic with edge cases

  Scenario: High income and excellent credit should cap at 850
    Given an applicant with income 200000, credit history 100, and 0 delinquencies
    When the risk score is computed
    Then the score should be 850

  Scenario: Missing income should default to 0
    Given an applicant with income 0, credit history 3, and 1 delinquencies
    When the risk score is computed
    Then the score should be 310

  Scenario: Missing credit history should default to 0
    Given an applicant with income 60000, credit history 0, and 2 delinquencies
    When the risk score is computed
    Then the score should be 320

  Scenario: Missing delinquencies should default to 0
    Given an applicant with income 45000, credit history 4, and 0 delinquencies
    When the risk score is computed
    Then the score should be 385

  Scenario: All fields missing or zero
    Given an applicant with income 0, credit history 0, and 0 delinquencies
    When the risk score is computed
    Then the score should be 300
