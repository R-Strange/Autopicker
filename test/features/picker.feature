Feature: picking an event

  Scenario: AI autopick with an event
    Given we have an event
    When we run it through an AI
    Then the AI will flag the event for us

  Scenario: AI autopick with noise
    Given we have noise
    When we run it through an AI
    Then the AI will not flag the event for us
    