import subprocess
import re
import csv
import datetime
from pathlib import Path

def get_battery_capacity_and_cycle_count():
    # Use ioreg command to get battery information
    ioreg_output = subprocess.check_output("ioreg -l | grep -E 'CycleCount|Capacity'", shell=True).decode('utf-8')

    # Extract the NominalChargeCapacity, DesignCapacity, and CycleCount values
    nominal_charge_capacity = int(re.search(r'"NominalChargeCapacity" = (\d+)', ioreg_output).group(1))
    design_capacity = int(re.search(r'"DesignCapacity" = (\d+)', ioreg_output).group(1))
    cycle_count = int(re.search(r'"CycleCount" = (\d+)', ioreg_output).group(1))

    # Calculate the maximum capacity percentage
    max_capacity_percentage = (nominal_charge_capacity / design_capacity) * 100

    return max_capacity_percentage, cycle_count

def log_battery_data_to_csv():
    max_capacity_percentage, cycle_count = get_battery_capacity_and_cycle_count()
    today_date = datetime.date.today().strftime("%Y-%m-%d")

    csv_file_path = "battery_data.csv"

    # Check if the CSV file exists, if not, create the file with headers
    if not Path(csv_file_path).is_file():
        with open(csv_file_path, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Date', 'Maximum Capacity', 'Cycle Count'])

    # Read the existing data
    with open(csv_file_path, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        existing_data = list(csv_reader)

    # Check if today's data already exists
    todays_data_index = None
    for index, row in enumerate(existing_data):
        if row and row[0] == today_date:
            todays_data_index = index
            break

    # Write the data back to the file, updating today's data if it exists
    with open(csv_file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date', 'Maximum Capacity', 'Cycle Count'])

        for index, row in enumerate(existing_data[1:]):
            if index + 1 == todays_data_index:
                # Overwrite today's data with the latest value
                csv_writer.writerow([today_date, f"{max_capacity_percentage:.2f}%", cycle_count])
            else:
                # Write the existing data
                csv_writer.writerow(row)

        if todays_data_index is None:
            # If today's data doesn't exist, append it
            csv_writer.writerow([today_date, f"{max_capacity_percentage:.2f}%", cycle_count])

if __name__ == "__main__":
    log_battery_data_to_csv()


# import subprocess
# import re
# import csv
# from pathlib import Path

# def get_battery_capacity_and_cycle_count():
#     # Use ioreg command to get battery information
#     ioreg_output = subprocess.check_output("ioreg -l | grep -E 'CycleCount|Capacity'", shell=True).decode('utf-8')

#     # Extract the NominalChargeCapacity, DesignCapacity, and CycleCount values
#     nominal_charge_capacity = int(re.search(r'"NominalChargeCapacity" = (\d+)', ioreg_output).group(1))
#     design_capacity = int(re.search(r'"DesignCapacity" = (\d+)', ioreg_output).group(1))
#     cycle_count = int(re.search(r'"CycleCount" = (\d+)', ioreg_output).group(1))

#     # Calculate the maximum capacity percentage
#     max_capacity_percentage = (nominal_charge_capacity / design_capacity) * 100

#     return max_capacity_percentage, cycle_count

# def log_battery_data_to_csv():
#     max_capacity_percentage, cycle_count = get_battery_capacity_and_cycle_count()

#     csv_file_path = "battery_data.csv"

#     # Check if the CSV file exists, if not, create the file with headers
#     if not Path(csv_file_path).is_file():
#         with open(csv_file_path, mode='w', newline='') as csvfile:
#             csv_writer = csv.writer(csvfile)
#             csv_writer.writerow(['Maximum Capacity', 'Cycle Count'])

#     # Append the data to the CSV file
#     with open(csv_file_path, mode='a', newline='') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow([f"{max_capacity_percentage:.2f}%", cycle_count])

# if __name__ == "__main__":
#     log_battery_data_to_csv()
