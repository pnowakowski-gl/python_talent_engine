def fix_month(date: str) -> str:
    date = date.split(".")
    date[1] = f"{(int(date[1]) + 1)}"
    date[1] = f"{'0'}" + f"{date[1]}" if len(date[1]) == 1 else f"{''}" + f"{date[1]}"
    return ".".join(date)


# Some quick tests
print(fix_month("19.09.2022 14:45"))  # '19.10.2022 14:45'
print(fix_month("11.0.2021"))  # '11.01.2021'
