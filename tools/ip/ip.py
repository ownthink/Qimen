import re

text = '我的ip是127.0.0.1'

ips = re.findall("(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])", text)

print(ips)
