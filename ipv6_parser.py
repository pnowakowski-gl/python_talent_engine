import re

text = """
    http://[2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d]:8080
    IP (analogue of ANY in IPv4) is ::
    Loopback address:  0000:0000:0000:0000:0000:0000:0000:0001
    Another localhost IPV6: ::1
    IPv4 in v6 is ::ffff:10.125.12.134
"""

def find_all_ipv6(text):
    found_ips = re.finditer(r"(([a-zA-Z0-9]{4}:){7}[a-zA-Z0-9]{4})|(::[\da-zA-Z]{,4}:?((\d{,3}\.){3}\d{,3})?)", text)
    print(re.findall(r"(([a-zA-Z0-9]{4}:){7}[a-zA-Z0-9]{4})|(::[\da-zA-Z]{,4}:?((\d{,3}\.){3}\d{,3})?)", text))
    return [ip.group(0) for ip in found_ips]


print(find_all_ipv6(text))
                                    