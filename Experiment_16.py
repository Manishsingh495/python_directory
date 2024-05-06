def is_right_triangle(a,b,c):
    if(((a*a + b*b)==c*c) or ((a*a + c*c)==b*b) or ((c*c + b*b)==a*a)):
        return "It is a right angle triangle" 
    else:
     return "It is not a right angle triangle" 


a=int(input('Enter 1st number: '))
b=int(input('Enter 2st number: '))
c=int(input('Enter 3st number: '))
print(is_right_triangle(a,b,c))