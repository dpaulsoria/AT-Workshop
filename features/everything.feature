Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "1|Acceptance Testing Workshop|Complete the workshop, the description is in AV|TODAY|Not Completed"
    Then the to-do list should contain "1|Acceptance Testing Workshop|Complete the workshop, the description is in AV|TODAY|Not Completed"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task ID       | Title                       | Description                                     | Due Date | Completed     |
      | 1             | Acceptance Testing Workshop | Complete the workshop, the description is in AV | TODAY    | Not Completed |
    When the user lists all tasks
    Then the output should contain:
      """
      ID: 1| Title: Acceptance Testing Workshop| Description: Complete the workshop, the description is in AV| Due Date: TODAY| Completed: Not Completed
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task ID       | Title                       | Description                                     | Due Date | Completed     |
      | 1             | Acceptance Testing Workshop | Complete the workshop, the description is in AV | TODAY    | Not Completed |
    When the user marks task "Acceptance Testing Workshop" as completed
    Then the to-do list should show task "Acceptance Testing Workshop" as completed

  Scenario: Save all tasks into a file
    Given the to-do list contains tasks:
      | Task ID       | Title                       | Description                                     | Due Date | Completed     |
      | 1             | Acceptance Testing Workshop | Complete the workshop, the description is in AV | TODAY    | Not Completed |
    When the user saves the tasks list into tasks.txt
    Then command line should show "All tasks saved."

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task ID       | Title                       | Description                                     | Due Date | Completed     |
      | 1             | Acceptance Testing Workshop | Complete the workshop, the description is in AV | TODAY    | Not Completed |
    When the user clears the to-do list
    Then the to-do list should be empty
