

import re
 
 
pattern = re.compile(u"1[34578]\d{9}")



text = '我的手机号是18896827613'

emails = re.findall(pattern, text)

print(emails)


