def firstUniqChar(s):
    if not s:
        return -1
    for index, ch in enumerate(s):
        if index == 0:
            if ch not in s[index+1:]:
                return index
        elif index == len(s)-1:
            if ch not in s[:-1]:
                return index
            else:
                return -1
        elif ch not in s[0:index] and ch not in s[index+1:]:
                return index
if __name__ == '__main__':
    s = "dddccdbba"
    print firstUniqChar(s)
