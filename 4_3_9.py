
print([value for value in range(1,21)])

listofnums = [value for value in range(1, 1000001)]
print(f"min = {min(listofnums)} max = {max(listofnums)}")
print(f"sum = {sum(listofnums)}")
listoddnum = [value for value in range(1,21,2)]
for value in listoddnum:
	print(value)


print([value for value in range(3,31,3)])
print([value**3 for value in range(1,11)])	
print(f"listoddnum = {listoddnum}")
print(f"The first three items in listoddnum are: {listoddnum[:3]}")
middlen=(int(len(listoddnum)/2))
print(f"Three items from the middle of the in listoddnum are: {listoddnum[middlen-1:middlen+3]}")
print(f"The last three items in listoddnum are: {listoddnum[-3:]}")