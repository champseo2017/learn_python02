# การทดสอบและยืนยัน
# โดย assert จะทําการตรวจสอบเงื่อนไขที่ใส่เข้าไปให้ โดยถ้าเงื่อนไขเป็น False จะทําให้โปรแกรม error ออกมา แต่ถ้าเงื่อนไขเป็น True ก็จะไม่มีอะไรเกิดขึ้น

def smallest_item(xs):
    assert xs, "empty list has no small item"
    return min(xs)


assert smallest_item([1]) == 1
