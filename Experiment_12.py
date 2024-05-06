# To find the average of a list of numbers using function
def Average(list):
    sum = 0
    for i in range(len(list)):
        sum=sum+list[i]
    print('The average of the numbers is ',sum/len(list))    

list=eval(input('Enter the elements of the list separated by comma : '))
Average(list)



