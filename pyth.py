# 1,1
# import os
# (os.remove('D:\s.txt'))

# 1.2
# import os
# (os.makedirs('D:\q.txt'))

# 1,3
# import os
# os.startfile(r'D:\123.txt')

# 1,4
# import os
# os.replace ('remove.txt','rem/remove.txt')

# 2
# input_str = input("Input list of integers here ")
# str = input_str.split(' ')
# ints = list(map(int, str))
# sum = 0
# for i in range(len(ints)):
#     sum = sum + ints[i]
# print("Result of sum = ",sum)

# 3
# def converter(str):
#     return int(str)
# my_input = ' 324 '
# print(type(my_input))
# print(converter(my_input))
# #check
# print(type(converter(my_input)))

# 4
# class Box:
#     def __init__(self, a, b):
#         self.side_a=a
#         self.side_b=b
        
#     def perimeter(self):
#         per = 2 *(self.side_a + self.side_b)
#         print("perimeter = ",per)
    
#     def area(self):
#         ar = (self.side_a * self.side_b)
#         print("area = ",ar)

# class Rectangle(Box):
#     def __init__(self, a, b):
#         super().__init__(a, b)

# recTangleArea = Rectangle(20,30).area()
# recTanglePerimeter = Rectangle(20,30).perimeter()  

