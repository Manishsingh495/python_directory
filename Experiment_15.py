# Take input string and store it in the list then print the string separated by comma using split function
#List_1=list(input('Enter a long string: '))
# Get input string from the user
input_string = input("Enter a string: ")


string_list =(list( input_string.split(",")))


#print("String separated by commas:", ", ".join(string_list))
print(string_list)
