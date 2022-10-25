list1 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "123124", "message": "DB stopped! Whatta hell!", "datetime": 1474456391},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "1223134", "message": "U hev bin pwned by hax0r tim!", "datetime": 1474624799},
    {"id": "1213234", "message": "Need more vespene gas!", "datetime": 1474624791},
]

list2 = [
    {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
    {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
    {"id": "3334113", "message": ""'; DELETE FROM customers WHERE 1 or username = '"; ", "datetime": 1474624789},
    {"id": "1213235", "message": "Require more minerals!", "datetime": 1474624792},
]
def merge_logs(list1, list2):
    ids = []
    resulted = list1 + list2
    a = [list2.remove(i) if i["id"] in ids else ids.append(i["id"]) for i in resulted]
    print(a)
    for i in resulted:
        if i["id"] in ids:
            list2.remove(i)
        else:
            ids.append(i["id"])
    resulted = list1 + list2
    return sorted(resulted, key=lambda datetime: datetime["datetime"])

print(merge_logs(list1, list2))