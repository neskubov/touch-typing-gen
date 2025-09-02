import random
import zipfile

num_of_characters = 10000 #Задаем количество символов

def gen_sequence_level_one(chars, length=1000):
    result = ""
    counter_symbols = 0
    max_weight = int(length // len(chars))
    grade_weight = {char:0 for char in chars}
    while counter_symbols < length:
        symbol = random.choice(chars)
        result += symbol + " "
        symbol_weight = grade_weight[symbol] + 1
        grade_weight[symbol] = symbol_weight
        if symbol_weight >= max_weight:
            chars = chars.replace(symbol, "")
        counter_symbols += 1
    return result


def gen_sequence_level_two(chars, length=1000):
    result = ""
    counter_symbols = 0
    while counter_symbols < length:
        length_word = random.randint(3, 11)
        for _ in range(length_word):
            symbol = random.choice(chars)
            result += symbol
            counter_symbols += 1
            if counter_symbols >= length:
                break
            result += " "

        counter_symbols += 1
    return result


tasks = [
    ("ваол", "seq1_level_one.txt", "seq1_level_two.txt"),
    ("ыдфж", "seq2_level_one.txt", "seq2_level_two.txt"),
    ("прен", "seq3_level_one.txt", "seq3_level_two.txt"),
    ("мьит", "seq4_level_one.txt", "seq4_level_two.txt"),
    ("кгуш", "seq5_level_one.txt", "seq5_level_two.txt"),
    ("цщйз", "seq6_level_one.txt", "seq6_level_two.txt"),
    ("сбчю", "seq7_level_one.txt", "seq7_level_two.txt"),
    ("я.э\\", "seq8_level_one.txt", "seq8_level_two.txt"),
    ("ёх-ъ", "seq9_level_one.txt", "seq9_level_two.txt")
]

# создаём текстовые файлы
for chars, fname_level_one, fname_level_two  in tasks:
    seq_level_one = gen_sequence_level_one(chars)
    seq_level_two = gen_sequence_level_two(chars, num_of_characters)
    with open(fname_level_one, "w", encoding="utf-8") as f:
        f.write(seq_level_one)
    with open(fname_level_two, "w", encoding="utf-8") as f:
        f.write(seq_level_two)

# упаковываем в архив
with zipfile.ZipFile("sequences.zip", "w") as zf:
    for _, fname_1, fname_2  in tasks:
        zf.write(fname_1)
        zf.write(fname_2)

print("Готово! Файл sequences.zip создан.")
