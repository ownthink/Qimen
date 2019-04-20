import re
 
 
pattern = re.compile("(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$")



text = '我的身份证是330702194706165014'

result = re.findall(pattern, text)

print(result)





