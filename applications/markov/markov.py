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
    start_word = True
    while start_word:
        first_word = random.choice(list(word_dict.keys()))
        if first_word[0] == first_word[0].upper() or first_word[0] == '"':
            start_word = False


    sentence = first_word

    choices = word_dict[first_word]

    random_word = random.choice(choices)

    sentence = sentence + f" {random_word}"

    while num_words != 0:
        choices = word_dict[random_word]

        random_word = random.choice(choices)

        sentence = sentence + f" {random_word}"

        num_words -= 1

        if num_words == 1:
            last_word_check = True
            while last_word_check:
                last_word = random.choice(list(word_dict.keys()))
                if last_word[-1] in ['.','?','!','"']:
                    sentence = sentence + f" {last_word}"
                    last_word_check = False
                    num_words -= 1

    print(f"Sentence: {_ + 1}")
    print(sentence, '\n')