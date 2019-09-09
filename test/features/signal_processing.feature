Feature: transforming an event

  Scenario: fourier transform an event
    Given we have data ready for fft analysis
    When we run an fft extract
    Then we will produce frequency-domain data

  Scenario Outline: decibellise the data
    Given we have <frequency-domain> data
    When we decibellise the data
    Then we change the data to a <normalised form>

    Examples: Single datapoints
       |  frequency-domain    | normalised form |
       |  1                   | 0               |
       |  10                  | 20              |
       |  100                 | 40              |
       |  0                   | False           |
       |  "string"            | False           |