def main():
    with open("books/frankenstein.txt") as f:
        frank = f.read()
    # print(frank)
    # print(countWords(frank))
    # print(countChars(frank))
    chars = countChars(frank)

    for c in chars.keys():
        if c.islower():
            print(f"The '{c}' character was found {chars[c]} times")


def countWords(s):
    return len(s.split())


def countChars(s):
    chars = dict()
    low = s.lower()

    for i in range(len(low)):
        c = low[i]
        if not c in chars.keys():
            chars[c] = 0
        chars[c] += 1

    return chars


if __name__ == "__main__":
    main()
