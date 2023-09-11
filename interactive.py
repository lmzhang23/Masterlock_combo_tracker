import new_num

obj = new_num.Combo()
num = obj.combo_list
combo = []
first_digit = ['1', '5', '9', '13', '17', '21', '25', '29', '33', '37']
second_digit = ['3', '7', '11', '15', '19', '23', '27', '31', '35']
for item in num:
    if item.split("-")[-1] == "37":
        if item.split("-")[0] in first_digit:
            if item.split("-")[1] in second_digit:
                combo.append(item)
print(len(combo))
print(combo)

answer_combo = ['17', '23', '37']
print(answer_combo)