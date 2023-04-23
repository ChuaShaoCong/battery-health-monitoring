import subprocess
import re

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

if __name__ == "__main__":
    max_capacity_percentage, cycle_count = get_battery_capacity_and_cycle_count()
    print(f"Maximum Capacity: {max_capacity_percentage:.2f}%")
    print(f"Cycle Count: {cycle_count}")



# import psutil

# battery_info = psutil._psplatform.sbattery_info()

# if battery_info is not None:
#     # Get the current battery capacity and maximum capacity
#     current_capacity = battery_info.percent
#     max_capacity = battery_info.maxcapacity

#     # Calculate the battery health percentage
#     battery_health = current_capacity / max_capacity * 100

#     print(f"Current Capacity: {current_capacity}%")
#     print(f"Maximum Capacity: {max_capacity}%")
#     print(f"Battery Health: {battery_health}%")
# else:
#     print("Battery not found.")


'''import psutil
import subprocess

def get_battery_capacity():
    # Get battery information using psutil
    battery_info = psutil.sensors_battery()
    
    # Get the current battery percentage
    current_capacity = battery_info.percent

    # Use pmset command to get the maximum capacity
    pmset_output = subprocess.check_output("pmset -g batt", shell=True).decode('utf-8')
    max_capacity_line = [line for line in pmset_output.split("\n") if "Design" in line]

    if max_capacity_line:
        max_capacity_str = max_capacity_line[0].split()[-1]
        max_capacity = float(max_capacity_str.rstrip('%'))
    else:
        max_capacity = 100.0  # Assume 100% if the information is not available

    return current_capacity, max_capacity

if __name__ == "__main__":
    current_capacity, max_capacity = get_battery_capacity()
    print(f"Current Capacity: {current_capacity}%")
    print(f"Maximum Capacity: {max_capacity}%")

'''