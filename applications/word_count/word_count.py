symb = ['"', ":", ";", ",", ".", "-", "+", "=", "/", "\\" "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\r", "\n", "\t"]
def word_count(s):
    count_dict  = {}
    for i in symb:
        s = s.replace(i, " ")

    if len(s) == 0:
        return {}
    
    s = s.lower()

    s = s.split(" ")

    for i in s:
        if i == '':
            pass
        elif i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    return count_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))