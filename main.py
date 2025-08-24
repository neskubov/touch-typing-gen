import random
import zipfile

num_of_characters = 10000 #Задаем количество символов

def gen_sequence(chars, length=1000):
    result = []
    for i in range(length):
        for num_space in range(random.randint(3, 11)):
            c = random.choice(chars)
            result.append(c)
        result.append(" ")
    return "".join(result)

tasks = [
    ("ваол", "seq1.txt"),
    ("ыдфж", "seq2.txt"),
    ("прен", "seq3.txt"),
    ("мьит", "seq4.txt"),
    ("кгуш", "seq5.txt"),
    ("цщйз", "seq6.txt"),
    ("сбчю", "seq7.txt"),
    ("я.э\\", "seq8.txt"),
    ("ёх-ъ", "seq9.txt"),
]

# создаём текстовые файлы
for chars, fname in tasks:
    seq = gen_sequence(chars, num_of_characters)
    print(seq)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(seq)

# упаковываем в архив
with zipfile.ZipFile("sequences.zip", "w") as zf:
    for _, fname in tasks:
        zf.write(fname)

print("Готово! Файл sequences.zip создан.")
