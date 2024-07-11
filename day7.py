## function in programing language  

# add two numbers 


# defination 
# def add_two(num1, num2):   # parameters
#     # return num1,num2 
#     output = num1 + num2
#     return output 


# a = int(input('enter first number : '))
# b = int(input('enter second number : '))

# calling 
# output = add_two(num1=a,num2=b)
# output = add_two(a,b)  # positional arguments
# print("Your addition is : ",output)




# print(len(ls))
# output = len(ls)
# print(output)

# define  
def my_len(ls):
    count = 0
    for item in ls:
        count += 1
    return count 

#calling 
rupees = [41,52,63,36,25,14,47,58,69,96,85,74]  # sum 

# print(my_len(ls=rupees))
# print(my_len(rupees))


def total_price(ls):
    total_sum = 0
    for item in ls:
        total_sum += item
    return total_sum 

print(total_price(rupees))

# average_finder()
# even_finder() 
# average_finder_even()
# my_min()
# my_max()
