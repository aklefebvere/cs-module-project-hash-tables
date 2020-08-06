import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

words = words.replace("\n", "")
words = words.split(' ')

word_dict = {}
for i in (words):
    if i not in word_dict:
        word_dict[i] = []
        for v, word in enumerate(words):
            if word == i:
                if v+1 < len(words):
                    word_dict[i].append(words[v+1])

# TODO: construct 5 random sentences
# Your code here


for _ in range(5):
    num_words = 15

    first_word = random.choice(list(word_dict.keys()))

    sentence = first_word

    choices = word_dict[first_word]

    random_word = random.choice(choices)

    sentence = sentence + f" {random_word}"

    while num_words != 0:
        choices = word_dict[random_word]

        random_word = random.choice(choices)

        sentence = sentence + f" {random_word}"

        num_words -= 1

    print(f"Sentence: {_ + 1}")
    print(sentence, '\n')