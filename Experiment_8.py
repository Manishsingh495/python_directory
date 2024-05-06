# To Add even digits of a number

a=int(input(' Enter a number= '))
a=str(a)
sum=0
for num in a:
    if(int(num)%2==0):
        sum += int(num)

print(sum)



