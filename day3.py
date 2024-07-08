### _________ BOOLEAN , LIST ______________

# var1 = True 
# var2 = False
# print(var1 , var2)
# print(type(var1) ,type(var2))



# list  
# array   
# int arr[10] = {1,2,3,5,5,6};

# ls = [25,41,36,74,25.2,21.,30.1,'upflairs',True]
# print(ls)
# print(type(ls))


# ls = [25,41,63,96,'upflairs',100]
# var = ls[4]
# print(var[4:7])

# mutable - changeble  (list)
# imutable - unchangeble  

# insert , remove , manipulate 
# student_name = ['taniya','yash','prerna','ruchika','aditya','kalika','yash']

# student_name[0] = "Tanya"  # manipulation or updation 
# student_name.append('jugnu')
# student_name.append('Ritu')  # at the last position 
# student_name.pop()  # it removes the item from the last position 
# student_name.insert(0,'gurpreet')
# student_name.remove('prernaa') 
# del student_name[2]

# print(student_name)
# print(student_name.count('yash'))

# ls1 = ['A','B','C','D','E']
# ls2 = [85,4,5,6,9,85,25,4,63,6,7]

# ls1.reverse()  # ls1[::-1]
# ls2.sort()  # asceding order 
# ls2.sort(reverse=True)
# print(ls2[::-1])
# ls1.sort()
# print(min(ls2))
# print(max(ls2))
# print(sum(ls2))


# ls1 = ['A','B','C','D','E']
# ls2 = ['F','G','H']
# full_list = ls1 + ls2
# print(full_list)
# ls1.append(ls2)
# ls1.extend(ls2)
# print(ls1)

# ls1 = ['A','B','C','D','E']
# ls1.clear()  
# print(ls1.index('C'))

# ls2 = [10,20,3.1,'upflairs pvt ltd',500,400]


# 3.1 = 100 
# 'upflairs pvt ltd'   = 'upflairs'
# 'upflairs pvt ltd'   = 'flipkart pvt ltd'


# >>>>>>>>>>>>  TUPLE   <<<<<<<<<<<<<<<<<
# imutable - unchangebl3  


# tpl = (25,41,63,96,'upflairs',True,25.2)
# del tpl[4]
# print(tpl)
# print(type(tpl))
# tpl[4] = 'flipkart'
# print(tpl)
# tpl.count()
# tpl.index()


# ls = []


# <<<<<<<<<<<<<<<<<,  SET   >>>>>>>>>>>>>>>>>>>>>>>>>>..

# st = {52,1,63,85,74,96,54,25,45,8,54,5,54,66,3,54}
# print(st[2])
# print(type(st))
# st.add(500)
# st.remove(540)   # 
# st.discard(54)   # 
# print(st)

# st1 = {52,41,63,96,78,54}
# st2 = {52,41,65,55,22}
# st1.update(st2)  # st1 + st2 


# print(st1.intersection(st2))

# <<<<<<<<<<<< DICTIONARY >>>>>>>>>>>>>... 
# pairs  = (key:value)

marks  = {'mohit':52,'rohit':56,'rocky':53,'mohit':54}
print(marks)
print(type(marks))

