
# ค่าความจริง
# ค่าความจริงใน python ทำงานเหมือนภาษาอื่นๆ ส่วนใหญ่ แต่ต้องใช้ตัวพิมพ์ใหญ่
one_is_less_than_two = 1 < 2  # equals True
true_equals_false = True == False  # equals False

# Python ใช้ค่า None เพื่อระบุการไม่มีค่า (คล้ายกับ null ภาษาอื่นเช่นกัน)
""" 
ทั้งสองคำสั่ง assert ใช้เพื่อ debugging และการทดสอบเงื่อนไขต่างๆ ในโค้ด เพื่อให้แน่ใจว่าค่าหรือสถานะของตัวแปรนั้นตรงตามที่ต้องการ. แต่คำสั่ง assert x is None เป็นวิธีที่แนะนำเพราะ is ใช้ตรวจสอบ identity ซึ่งเหมาะสมกว่าในการตรวจสอบ None.
"""
x = None
assert x == None
assert x is None

s = "some_function_that_returns_a_string()"
if s:
    first_char = s[0]
else:
    first_char = ""

# and จะคืนค่าที่สอง หากสิ่งแรกเป็น จริง และ คืนค่าแรก ถ้าไม่เป็นจริง
first_char = s and s[0]
print(first_char)
