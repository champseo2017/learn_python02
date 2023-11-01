# Tuple
# มีลักษณะคล้ายกับ List ทุกอย่างที่ทำกับ List สามารถทำได้กับ Tuple
# ยกเว้นการแก้ไข จะใช้ วงเล็บ หรือ ไม่ใช้ วงเล็บก็ได้

my_list = [1, 2]  # list เป็น mutable สามารถแก้ไขได้
my_tuple = (1, 2)  # Tuple ไม่สามารถแก้ไขได้ เป็น immutable
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")
# Tuple ถือเป็นวิธีที่สะดวกในการคืนค่าหลายค่าจากฟังก์ชัน


def sum_and_product(x, y):
    return (x + y), (x * y)  # Tuple


sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

# กำหนดค่าแบบหลายรายการ
x, y = 1, 2
x, y = y, x
