# f-string แทนค่าลงในเงื่อนไข
first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name
full_name2 = "{0}{1}".format(first_name, last_name)
full_name3 = f"{first_name} {last_name}"
print(full_name3)
