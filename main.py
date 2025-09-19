import random
import zipfile
import os
# import psutil
# process = psutil.Process(os.getpid())
# print(f"Использование памяти: {process.memory_info().rss / 1024 ** 2:.2f} MB")

num_of_characters = 5000 #Задаем количество символов

def gen_sequence_level_one(chars, length=1000):
    result = ""
    counter_symbols = 0
    choice_chars = chars
    while counter_symbols < length:
        symbol = random.choice(choice_chars)
        result += symbol + " "

        choice_chars = choice_chars.replace(symbol, "")

        if not choice_chars:
            choice_chars = chars

        counter_symbols += 1

    return result


def gen_sequence_level_two(chars, length=1000):
    result = chars
    counter_symbols = 0
    while counter_symbols < length:
        length_word = random.randint(3, 11)
        for _ in range(length_word):
            symbol = random.choice(chars)

            if result[-1] == symbol:
                continue

            result += symbol
            counter_symbols += 1

            if counter_symbols >= length:
                break

        result += " "
        counter_symbols += 1

    return result


tasks = [
    "ваол",
    "ыдфж",
    "ваолыдфж",
    "прен",
    "ыдфжпрен"
    "ваолыдфжпрен",
    "мьит",
    "пренмьит",
    "ыдфжпренмьит",
    "ваолыдфжпренмьит",
    "кгуш",
    "мьиткгуш",
    "пренмьиткгуш",
    "ыдфжпренмьиткгуш",
    "ваолыдфжпренмьиткгуш",
    "цщйз",
    "кгушцщйз",
    "мьиткгушцщйз",
    "пренмьиткгушцщйз",
    "ыдфжпренмьиткгушцщйз",
    "ваолыдфжпренмьиткгушцщйз",
    "сбчю",
    "цщйзсбчю",
    "кгушцщйзсбчю",
    "мьиткгушцщйзсбчю",
    "сбчюпренмьиткгушцщйз",
    "сбчюыдфжпренмьиткгушцщйз",
    "сбчюваолыдфжпренмьиткгушцщйз",
    "я.э\\",
    "я.э\\сбчю",
    "я.э\\цщйзсбчю",
    "я.э\\кгушцщйзсбчю",
    "я.э\\мьиткгушцщйзсбчю",
    "я.э\\сбчюпренмьиткгушцщйз",
    "я.э\\сбчюыдфжпренмьиткгушцщйз",
    "я.э\\сбчюваолыдфжпренмьиткгушцщйз",
    "ёх-ъ",
    "ёх-ъя.э\\",
    "ёх-ъя.э\\сбчю",
    "ёх-ъя.э\\цщйзсбчю",
    "ёх-ъя.э\\кгушцщйзсбчю",
    "ёх-ъя.э\\мьиткгушцщйзсбчю",
    "ёх-ъя.э\\сбчюпренмьиткгушцщйз",
    "ёх-ъя.э\\сбчюыдфжпренмьиткгушцщйз",
    "ёх-ъя.э\\сбчюваолыдфжпренмьиткгушцщйз"
         ]

# создаём текстовые файлы
number_file = 1
with zipfile.ZipFile("sequences.zip", "w") as zf:
    for chars in tasks:
        fname_level_one = f'seq_{number_file}_level_one.txt'
        fname_level_two = f'seq_{number_file}_level_two.txt'

        seq_level_one = gen_sequence_level_one(chars, num_of_characters)
        seq_level_two = gen_sequence_level_two(chars, num_of_characters)

        with open(fname_level_one, "w", encoding="utf-8") as f:
            f.write(seq_level_one)

        with open(fname_level_two, "w", encoding="utf-8") as f:
            f.write(seq_level_two)

        zf.write(fname_level_one)
        zf.write(fname_level_two)

        os.remove(fname_level_one)
        os.remove(fname_level_two)

        number_file += 1

print("Готово! Файл sequences.zip создан.")
