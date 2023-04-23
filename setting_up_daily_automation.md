
# Setting Up Automation for Running a Python Script Daily on macOS

This guide will walk you through the steps to set up automation to run a Python script daily on your macOS using Automator and Calendar.

## Steps
1. Open Automator from the Applications folder.
2. In the search field, type "Run Shell Script" and drag it to the workflow area on the right.
3. Change "Pass input" to "as arguments".
4. In the script window, type the shell command to run your Python script, for example: 
    * ```cd /path/to/your/directory/ ```
    * ```python3 battery_data_logger.py```

    Make sure to replace ```/path/to/your/directory/``` and ```battery_data_logger.py``` with the actual path to your Python script and the script name.

5. Save the workflow as an application by choosing "File" > "Save" and giving it a name.
6. Open the Calendar app, and create a new event by clicking the "+" button.
7. Set the event to repeat daily.
8. In the "Alert" section, choose "Custom" and select the workflow application you created in step 5.
9. Set the alert time to be the time of day you want the app to run.
10. Save the event and close the Calendar app.
