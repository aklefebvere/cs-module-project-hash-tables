def no_dups(s):
    dupe_dict = {}
    if s == "":
        return ""

    s = s.split(" ")

    for i in s:
        if i not in dupe_dict:
            dupe_dict[i] = i

    dupe_list = list(dupe_dict.keys())

    s = " ".join(dupe_list)

    return s
    

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))