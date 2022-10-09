# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
from random import sample


def create_str(num: int, word: str = 'абв'):
    if num <= 0:
        print("Data is incorrect. Try again.")
    st = []
    for i in range(num):
        one_piece = sample(word, 3)
        st.append("".join(one_piece))
    return " ".join(st)


def del_word(text: str):
    return text.replace("абв ", "")


res = del_word(create_str(int(input("Enter the number of words: "))))

print(res)
