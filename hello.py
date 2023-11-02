from collections import defaultdict

# defaultdict
# สร้าง dictionary ที่ชื่อว่า word_counts เพื่อจัดเก็บจำนวนคำ
""" 
`split()` คือเมธอดใน Python ที่ใช้แยกสตริงเป็นลิสต์ของคำโดยใช้ตัวแยก (delimiter) ที่กำหนด หากไม่ได้กำหนดตัวแยก, `split()` จะใช้ช่องว่างเป็นตัวแยกโดยปริยาย. 

ใน code `document = "the quick brown fox jumps over the lazy dog".split()` นี้, `split()` จะแยกสตริง `"the quick brown fox jumps over the lazy dog"` ให้เป็นลิสต์ของคำ `[ "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]` และเก็บลิสต์นี้ในตัวแปร `document`.

"""
word_counts = {}

# กำหนด document เป็นตัวแปรที่มีข้อมูลตัวอักษรหรือคำ
document = "the quick brown fox jumps over the lazy dog".split()

# วน loop ทำงานในแต่ละคำที่อยู่ใน document
for word in document:
    # ตรวจสอบว่าคำนี้มีอยู่ใน dictionary word_counts หรือไม่
    if word in word_counts:
        # ถ้ามี, เพิ่มจำนวนนับของคำนี้ใน dictionary 1 หน่วย
        word_counts[word] += 1
    else:
        # ถ้าไม่มี, เพิ่มคำนี้ลงใน dictionary ด้วยค่านับเป็น 1
        word_counts[word] = 1

# พิมพ์ dictionary word_counts แสดงผลลัพธ์
# print(word_counts)

# ใช้  except KeyError
word_counts2 = {}
for word in document:
    try:
        word_counts2[word] += 1
    except KeyError:
        word_counts2[word] = 1
# print(word_counts2)

# ใช้ get ทำงานกับคีย์ที่ยังไม่มี
word_counts3 = {}
for word in document:
    previous_count = word_counts3.get(word, 0)
    word_counts3[word] = previous_count + 1

# print(word_counts3)

""" 
1. `word_counts4 = defaultdict(int)`: สร้าง `defaultdict` ที่ชื่อ `word_counts4` โดยมีค่าเริ่มต้นเป็น 0 (เพราะ `int()` จะคืนค่า 0).
2. `for word in document:`: วนลูปทำงานในแต่ละคำที่อยู่ใน `document`.
3. `word_counts[word] += 1`: เพิ่มจำนวนนับของคำนี้ใน `word_counts4` 1 หน่วย.

จะเห็นว่าในโค้ดนี้ไม่ต้องมีการตรวจสอบ `if word in word_counts4:` เพราะ `defaultdict` จะสร้างคีย์ใหม่โดยอัตโนมัติกับค่าเริ่มต้นเป็น 0 ถ้าคีย์นั้นยังไม่มีอยู่.

"""
word_counts4 = defaultdict(int)
for word in document:
    word_counts[word] += 1
