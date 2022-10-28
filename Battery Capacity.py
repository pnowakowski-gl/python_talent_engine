import re

data = """
        "SuperMaxCapacity" =0
        "MaxCapacity": +4540;
        'CurrentCapacity'=   2897,
        "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
        "MegaMaxCapacity" = 6700
"""


def get_battery_level(data):
    maxCapacity = re.findall(r"\WMaxCapacity\D+(\d+)", data)[0]
    currentCapacity = re.findall(r"CurrentCapacity\D+(\d+)", data)[0]
    currentBattery = int(currentCapacity) / int(maxCapacity) * 100
    return f"{currentBattery:.2f}%"


print(get_battery_level(data))
