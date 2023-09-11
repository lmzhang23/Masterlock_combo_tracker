from itertools import permutations

num = []
class Combo:
    def __init__(self):
        self.digits = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
        self.n = 3
        self.length = len(self.generate_all_combo())
        self.combo_list= self.generate_all_combo()
        self.wrong_list= []
        self.answer_combo = ''

    def generate_all_combo(self):
        combo_list = ['-'.join(map(str, p)) for p in permutations(self.digits, self.n) if p[0] != 0]
        return combo_list

    def remove_wrong_combo(self, combo_list: list, wrong_combo: str) -> object:
        self.combo_list.remove(wrong_combo)
        self.wrong_list.append(wrong_combo)
        self.length -= 1



