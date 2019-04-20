
import re
 
regex = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

text = '我的邮箱是1268@qq.com'

emails = re.findall(regex, text)

print(emails)