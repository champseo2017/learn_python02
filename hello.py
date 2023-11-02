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


# ใช้ method get ส่งค่าเริ่มต้นกลับมา เมื่อค่าคีย์ไม่อยู่ใน Dictionary
joels_grade = grades.get("Joel", 0)  # equals 80
kates_grade = grades.get("Kate", 0)  # equals 0
no_ones_grade = grades.get("No One")  # default is None

# กำหนดคีย์ / ค่า ใน []
grades["Tim"] = 99  # replaces the old value
grades["Kate"] = 100  # adds a third entry
num_students = len(grades)  # equals 3

# ใช้ Dictionary เก็บข้อมูลที่มีโครงสร้าง
tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data"]
}

# ดู key ทั้งหมด
tweet_keys = tweet.keys()  # iterable for the keys
tweet_values = tweet.values()  # iterable for the values
tweet_items = tweet.items()  # iterable for the (key, value) tuples

"user" in tweet_keys  # True, but not Pythonic
"user" in tweet  # Pythonic way of checking for keys
"joelgrus" in tweet_values  # True (slow but the only way to check)
