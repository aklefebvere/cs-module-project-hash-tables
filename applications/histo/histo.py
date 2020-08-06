# Your code here

with open("applications/histo/robin.txt") as f:
    words = f.read()


# words = words.replace("\n", "")
# words = words.split(' ')


symb = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\" "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\r", "\n", "\t"]
def word_count(s):
    count_dict  = {}
    for i in symb:
        s = s.replace(i, " ")
    
    s = s.lower()

    s = s.split(" ")

    for i in s:
        if i == '':
            pass
        elif i in count_dict:
            count_dict[i] = count_dict[i] + "#"
        else:
            count_dict[i] = "#"

    sort_by_val = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    len_val_checker = {}

    for i in sort_by_val:
        sort_by_name = []
        len_val = len(i[1])
        if len_val not in len_val_checker:
            len_val_checker[len_val] = len_val
            for v in sort_by_val:
                if len(v[1]) == len_val:
                    sort_by_name.append(v)
            if len(sort_by_name) > 1:
                sorted_names = sorted(sort_by_name, key=lambda x: x[0])
                for name in sorted_names:
                    spaces = " " * (17 - len(name[0]))
                    print(f"{name[0]}{spaces}{name[1]}")
            else:
                spaces = " " * (17 - len(i[0]))
                print(f"{i[0]}{spaces}{i[1]}")


word_count(words)