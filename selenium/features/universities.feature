Feature: Search for degree programs on university websites

  Scenario Outline: Search for degree programs using the university internal search bar
    Given I open the Chrome browser
    When I search for "<university>" on Google
    Then I should see the official link for "<university>" in the results
    And I click on the first result for "<university>"
    And I verify that I am on the "<university>" website
    And I search for "carreras" using the internal search bar
    Then I should see results related to "carreras"

    Examples:
      | university        |
      | ITESO             |
      | UNAM              |
      | Tec de Monterrey  |
