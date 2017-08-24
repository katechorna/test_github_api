Feature: Gists

Scenario: Create gist
    Given we verified number of existing gists
    Then we create new gist
    Then we check if number of gists is increased by one
    Then we delete newly created gist
