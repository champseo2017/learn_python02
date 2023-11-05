from collections import defaultdict

""" 
เมื่อคุณใช้คำสั่ง `dd_pair[2][1] = 1`, มันจะทำหลายขั้นตอน:

1. Python จะตรวจสอบว่า `dd_pair` มี key `2` หรือไม่. ในกรณีนี้, `dd_pair` ยังไม่มี key `2`, ดังนั้นมันจะใช้ฟังก์ชัน factory (`lambda: [0, 0]`) เพื่อสร้างค่าเริ่มต้นสำหรับ key `2`, ซึ่งคือ `[0, 0]`.

2. ต่อจากนั้น, มันจะใช้ index `1` เพื่อเข้าถึงสมาชิกที่สองของรายการ `[0, 0]`, และจากนั้นมันจะตั้งค่าสมาชิกนี้เป็น `1`.

ผลลัพธ์คือ `dd_pair` ตอนนี้มีค่าเป็น `{2: [0, 1]}`.

"""

dd_list = defaultdict(list)  # list() ผลิตรายการที่ว่างเปล่า
dd_list[2].append(1)  # now dd_list contains {2: [1]}
dd_dict = defaultdict(dict)  # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1  # now dd_pair contains {2: [0, 1]}
