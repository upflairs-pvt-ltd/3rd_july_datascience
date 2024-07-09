# marks  = {'rakesh':52,'rohit':56,'rocky':53,'mohit':54}
# print(marks)
# print(type(marks))
# var['key']
# print(marks['rakesh'])  # 
# print(marks['mohit']) 


# print(marks['rohit'])
# marks['rohit'] = 66
# marks['rahul'] = 100   #   'rahul':100  insert operation 
# print(marks.keys())
# print(marks.values())

 
# marks.pop('rohit')

# print(marks)



# students = {'Name':['rahul','mohit','ritu','yash','jugnu'],
#             'Marks':[52,14,36,45,96],
#             'Subject':"Science"}  


# students['Subject'] = "physics"
# print(students['Subject'])
# print(type(students))



# science_marks = {'Name':['rahul','mohit','ritu','yash','jugnu'],
#             'Marks':[52,14,36,45,96],
#             'Subject':"Science"}  


# science_marks['Name'].remove('mohit')
# science_marks['Marks'].remove(14)


# science_marks['Marks'][1] = 41

# print(science_marks)







# science_marks['Name'].remove('ritu')
# science_marks['Marks'].remove(36)

# science_marks['Name'].pop(2)
# science_marks['Marks'].pop(2)

# print(science_marks)
# print(science_marks['Name'])
# print(type(science_marks['Name']))


# <<<<<<<<<<<< type casting  >>>>>>>>>>>>>>>>>> 
# int() , float()  , str() , tuple() , list() , dict() , set()
# num1 = 10   

# num1 = float(num1)
# print(num1)
# print(type(num1))


# num2 = 20.25
# num2 = int(num2)
# print(num2)
# print(type(num2))

# ls = [10,1,0,10,10,20,30,40,40,50,60,70,80,80,90]
# ls = list(set(ls))
# print(ls)



# _________ OPERATORS  _____________

# # 1. Arithmatic operators  
# num1 = int(input('Plz enter first number : '))
# num2 = int(input('Plz enter second number : '))
# output = num1 % num2   # % , **   
# output = num1 ** num2 
# print(output)
# 9 % 3 = 0 
# 10 % 3 = 1   


# num1 = int(num1)
# num2 = int(num2)

# print(type(num1))
# print(type(num2))



num1 = int(input('Plz enter first number : '))
num2 = int(input('Plz enter second number : '))
output = num1 ** num2 
print(output)