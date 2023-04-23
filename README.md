# Battery Data Logger

This tool is part of a larger project aimed at testing different strategies to maximize battery lifespan health.

The macOS System Information solely provides information on the current state of the battery, and doesn't preserve a historical log. This script extracts and logs the data daily to enable better tracking of the battery's health over time and detect any issues or degradation

## How it works

This script logs the maximum capacity percentage and cycle count of a MacBook's battery. The data is stored in a CSV file called `battery_data.csv`. The script ensures that only one entry is logged per day, and if the script is run multiple times within the same day, it will use the latest value and overwrite the previous value for that day.

## Requirements

- Python 3
- macOS (tested on macOS Big Sur and later)

## Usage

1. Open Terminal.
2. Navigate to the folder containing the script (e.g., `cd /path/to/script`).
3. Run the script using the following command: python3 battery_data_logger.py

The script will create or update the `battery_data.csv` file in the same folder, logging the date, maximum capacity percentage, and cycle count of the MacBook's battery.

## Columns in the CSV file

- `Date`: The date when the script was run (YYYY-MM-DD).
- `Maximum Capacity`: The percentage of the maximum capacity of the battery compared to its design capacity.
- `Cycle Count`: The number of charge-discharge cycles the battery has gone through.

## Troubleshooting

If you encounter any issues, make sure you have the required permissions to read battery information and write files in the folder containing the script. Also, check that your macOS version is supported by the script. The Terminal commands used in the script may change over time as macOS gets updated, so you might need to look for updated commands if you're using a newer version of macOS.


