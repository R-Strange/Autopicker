Feature: inputting data and receiving data and context back

  Scenario Outline: Inputted data should be checked for viability
    Given an <input file>
    When we analyse the viability of the file
    Then we can print any <errors>
    And we can <forward the data> to the next step if it is viable
    And we can <fail gracefully> if the data is not viable

    Examples: Input Files
      | input file     | errors | forward the data | fail gracefully |
      | correct.csv    | False  | True             | False           |
      | correct.json   | False  | True             | False           |
      | correct.sac    | False  | True             | False           |
      | correct.wav    | False  | True             | False           |
      | incorrect.csv  | True   | False            | True            |
      | incorrect.json | True   | False            | True            |
      | incorrect.sac  | True   | False            | True            |
      | incorrect.wav  | True   | False            | True            |
      | no_extension   | True   | False            | True            |

  Scenario Outline: Providing viable input data should provide the events as an output
    Given a <viable input file>
    When we autopick the data
    Then we print back the <number of found events>
    And we produce a <number of event files> equal to the number of reported events
    And if we have bad data we <fail gracefully>

    Examples: Viable Input Files
    | viable input file | number of found events | number of event files | fail gracefully |
    | one.csv           | 1                      | 1                     | False           |
    | one.json          | 1                      | 1                     | False           |
    | one.sac           | 1                      | 1                     | False           |
    | one.wav           | 1                      | 1                     | False           |
    | ten.csv           | 10                     | 10                    | False           |
    | ten.json          | 10                     | 10                    | False           |
    | ten.sac           | 10                     | 10                    | False           |
    | ten.wav           | 10                     | 10                    | False           |
    | none.csv          | 0                      | 0                     | False           |
    | none.json         | 0                      | 0                     | False           |
    | none.sac          | 0                      | 0                     | False           |
    | none.wav          | 0                      | 0                     | False           |
    | fail.csv          | 0                      | 0                     | True            |
    | fail.json         | 0                      | 0                     | True            |
    | fail.sac          | 0                      | 0                     | True            |
    | fail.wav          | 0                      | 0                     | True            |