# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
from random import sample


def create_str(num: int, word: str = 'абв'):
    st = []
    for i in range(num):
        one_piece = sample(word, 3)
        st.append("".join(one_piece))
    return " ".join(st)


def del_word(strn: str):
    return strn.replace(" абв", "")


res = create_str(int(input("Enter the number of words: ")))

print(res)

