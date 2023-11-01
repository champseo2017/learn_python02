# Dictionary เชื่อมโยงค่าต่างๆ กับคีย์ สามารถดึงค่าที่สอดคล้องกับ คีย์ที่กำหนด
empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

# หาค่าของคีย์โดยใช้วงเล็บเหลี่ยม
joels_grade = grades["Joel"]


# ได้รับ keyError หากเรียกใช้คีย์ที่ไม่มีอยู่ใน Dictionary
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# ตรวจสอบการมีอยู่ของคีย์ได้โดยใช้คำสั่งนี้
joel_has_grade = "Joel" in grades  # True
kate_has_grade = "Kate" in grades  # False
