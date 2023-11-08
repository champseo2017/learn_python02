
# Set เก็บชุดขององค์ประกอบที่แตกต่างกัน กำหนดด้วยวงเล็บปีกกา
primes_below_10 = {2, 3, 5, 7}

s = set()
s.add(1)  # s is now {1}
s.add(2)  # s is now {1, 2}
s.add(2)  # s is still {1, 2}
# x = len(2)  # equals 2
y = 2 in s  # equals True
z = 3 in s  # equals False

# ใช้ set ด้วยหลัก 2 ประการ 1. in จะทำงานได้เร็วมากกับ set หากมีข้อมูลจำนวนมาก
# การใช้ set จะเหมาะสมกว่า list

stopwords_list = ["a", "an", "at"] + ["yet", "you"]
"zip" in stopwords_list  # False, but have to check every element
stopwords_set = set(stopwords_list)
"zip" in stopwords_set  # very fast to check

# ใช้ค้นหารายการที่แตกต่างกัน
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_item_list = list(item_set)

print(item_set)
