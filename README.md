# Battery Data Logger

This script logs the maximum capacity percentage and cycle count of a MacBook's battery. The data is stored in a CSV file called `battery_data.csv`. The script ensures that only one entry is logged per day, and if the script is run multiple times within the same day, it will use the latest value and overwrite the previous value for that day.

## Requirements

- Python 3
- macOS (tested on macOS Big Sur and later)

## Usage

1. Open Terminal.
2. Navigate to the folder containing the script (e.g., `cd /path/to/script`).
3. Run the script using the following command:

