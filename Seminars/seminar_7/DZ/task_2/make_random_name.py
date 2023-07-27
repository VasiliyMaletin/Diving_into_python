from random import randint, choices

VOLEWELS = 'аеиоуяюёэы'
CONSONANTS = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1) if chr(char) not in VOLEWELS])


def make_random_name(amount_of_names: int):
    count = 0
    all_names = []
    while count != amount_of_names:
        word_len = randint(4, 7)
        word = choices(VOLEWELS + CONSONANTS, k=word_len)
        if any(ch in VOLEWELS for ch in word):
            all_names.append(''.join(word).capitalize() + '\n')
            count += 1
    with open('task_2.txt', 'a', encoding='utf-8') as f:
        f.writelines(all_names)


make_random_name(10)
