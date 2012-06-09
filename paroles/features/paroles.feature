Feature: public site

  As a visitor
  I browse parole2 website to see the paroles

  Scenario: visitors goes to index
    Given I go to the url "/"
    Then I should see the header "Parole2"
