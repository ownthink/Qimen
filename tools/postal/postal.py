

import re
 
 
pattern = re.compile("[1-9]\d{5}(?!\d)")



text = '我的邮政编码是215000'

result = re.findall(pattern, text)

print(result)





