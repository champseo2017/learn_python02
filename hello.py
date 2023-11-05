# Counter เปลียนลำดับของค่าให้เป็น คีย์ และ นับจำนวนให้ด้วย
from collections import Counter
c = Counter([0, 1, 2, 0])  # c is (basically) {0: 2, 1: 1, 2: 1}

document = "the quick brown fox jumps over the lazy dog".split()
word_counts = Counter(document)

# most_common
# print the 10 most common words and their counts
""" 
1. `document = "the quick brown fox jumps over the lazy dog".split()` จะสร้าง `document` เป็นรายการของคำจากสตริงที่กำหนด, โดยใช้ `split()` เพื่อแยกคำตามช่องว่าง.

2. `word_counts = Counter(document)` จะสร้างออบเจ็กต์ `Counter` จากรายการ `document`, ทำให้ `word_counts` นับจำนวนครั้งของแต่ละคำที่ปรากฏใน `document`.

3. `for word, count in word_counts.most_common(10):` จะวนลูปผ่าน 10 คู่คำที่มีจำนวนครั้งสูงสุดใน `word_counts` (ในกรณีนี้, มีแค่ 9 คำที่ไม่ซ้ำกันใน `document`, ดังนั้นลูปจะวนเพียง 9 ครั้ง).

4. `print(word, count)` จะพิมพ์คำและจำนวนครั้งที่คำนั้นปรากฏใน `word_counts` ลงในคอนโซล.

"""
for word, count in word_counts.most_common(10):
    print(word, count)
