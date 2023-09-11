
import random
import new_num

obj = new_num.Combo()
num = obj.combo_list
combo=[]
first_digit=['1','5','9','13','17','21','25','29','33','37']
second_digit = ['3','7','11','15','19','23','27','31','35']
for item in num:
    if item.split("-")[-1]=="37":
        if item.split("-")[0] in first_digit:
            if item.split("-")[1] in second_digit:
                combo.append(item)

num=combo
print(len(num))
answer_combo = ['17', '23', '37']
print(f"pss the lock combo was {answer_combo}")




is_locked = True

guess = random.sample(num, 1)
print(''.join(guess))
is_guess_right = input(f"Did {guess} work? enter T/F").upper()
attempt = 0

while is_guess_right == "F":
    guess_element = ''.join(guess)
    guess_index = num.index(''.join(guess))
    no_good_guess = num.pop(guess_index)
    attempt += 1
    print(f"You have tried {attempt} time(s) so far")
    obj.remove_wrong_combo(num, no_good_guess)
    guess = random.sample(num, 1)
    is_guess_right = input(f"Did {guess} work? enter T/F").upper()
else:
    print(f"You have guessed {guess} and it is right!")
    obj.answer_combo.replace(obj.answer_combo, ''.join(guess))
    print(obj.answer_combo)
    is_locked = False

print(f"In total, you have tried and eliminated {attempt} times in this set.")

