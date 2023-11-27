s = input()
print(s)
first = s.find('h')
last = s.rfind('h')
print(first, last)
if first != -1 and last != -1:
    s = s[first+1]+s[first+1:last].replace('h', 'H')+s[last]
print(s)