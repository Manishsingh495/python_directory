# Write a program using split function to accept a group of numbers and find their average( without using loop construct)

x=list(input('Enter the numbers= ').split(","))
# we can also use code of line 5 instead of line 3 both works same
# x=[int(x)for x in input().split(",")]
'''y=len(x)
Sum1=sum(x)
print('Average of numbers is=',Sum1/y)'''
print(x)