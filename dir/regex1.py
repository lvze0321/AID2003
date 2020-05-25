"""
ｒｅ模块使用
"""
import re

# 目标字符串
s = "Alex:1997,Sunny:1995"
pattern = "(\w+):(\d+)"

# 如果正则表达式有子组，则只返回子组对应部分
result = re.findall(pattern,s)
print(result)

# 使用正则表达式切割字符串
result  = re.split(r':|,',s,2)
print(result)

# 使用字符串替换匹配到的部分  使用"xxx"替换s中匹配到的部分
result = re.sub("\d+","xxx",s,1)
print(result)


