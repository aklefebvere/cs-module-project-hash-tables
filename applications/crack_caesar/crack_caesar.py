# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()


replace_chars = [" ", '"', ",", ".", "!", '\n', "'", ":", ";", "(", ")", "-", '—', '?', "1"]
letters = words
for char in replace_chars:
    letters = letters.replace(char, "")


frequency_chars = {}

for i in letters:
    if i not in frequency_chars:
        frequency_chars[i] = 1
    else:
        frequency_chars[i] = frequency_chars[i] + 1

    
sorted_chars = sorted(frequency_chars.items(), key=lambda x: x[1], reverse=True)


# print(sorted_chars)

frequency_keys = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

caesar_map = {}

for i, j in zip(frequency_keys, sorted_chars):
    caesar_map[j[0]] = i

new_str = ""
for i in words:
    if i in caesar_map:
        new_str = new_str + caesar_map[i]
    else:
        new_str = new_str + i


print(new_str)

