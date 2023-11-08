
# ควบคุมการทำงาน
# สามารถดำเนินการตามเงื่อนไขได้โดยใช้คำสั่ง if
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "when all else fails use else (if you want to)"
else:
    message = ""

# เขียนคำสั่ง if-then-else ได้ในบรรทัดเดียวกัน

x = 10
parity = "even" if x % 2 == 0 else "odd"

# ใช้ while สำหรับการวนซ้ำ
x = 0
# while x < 10:
#     print(f"{x} is less than 10")
#     x += 1

# หลายครั้งเราจะใช้ for และ in
# for x in range(10):
#     print(f"{x} is less than 10")

# ถ้าต้องการเงื่อนไขที่ซับซ้อนขึ้น สามารถใช้ continue และ break
for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break  # quit the loop entirely
    print(x)
# แสดงตัวเลข 0, 1, 2 และ 4
