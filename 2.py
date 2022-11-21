def occurance(ch, st):
	if (len(st) == 0):
		return 0
	count = 0
	if (st[0] == ch):
		count += 1
	count += occurance(ch, st[1:])
	return count
	
str1 = input()
str2=input()
c = str2[-1]
print(occurance(c, str1))
