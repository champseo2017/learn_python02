# List
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_list = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)
list_sum = sum(integer_list)
# print(list_sum)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0]
one = x[1]
nine = x[-1]
# print(nine)

"""
ใน Python, โค้ด `x[:3]` ใช้เพื่อดึงข้อมูลจากรายการ `x` โดยเริ่มต้นจาก index ที่ `0` และหยุดที่ index ที่ `3` (แต่ไม่รวม index ที่ `3`). ดังนั้น, `first_three` จะได้รับค่า `[0, 1, 2]`.
"""
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]
print(copy_of_x)
every_third = x[::3]
""" 
โค้ด five_to_three = x[5:2:-1] ใน Python หมายถึงการตัด list x โดยเริ่มจาก index 5 ไปยัง index 2 (แต่ไม่รวม index 2) และด้วย step -1 ซึ่งหมายความว่าการกระโดดย้อนกลับไป 1 index ในแต่ละ step.
"""
five_to_three = x[5:2:-1]
print(every_third)
