def countWords(s: str) -> int:
    count = len(s.split())

    return count


def countChars(s: str) -> dict[str, int]:
    chars = {}
    low = s.lower()

    for i in range(len(low)):
        c = low[i]
        if not c in chars.keys():
            chars[c] = 0
        chars[c] += 1

    return chars


def sortChars(chars: dict[str, int]) -> list[dict[str, int]]:

    def sort_on(d: dict[str, int]):
        return next(iter(d.values()))

    lst = list(map(lambda c: {c: chars[c]}, chars))
    lst.sort(reverse=True, key=sort_on)

    return lst


def filterChars(chars: dict[str, int]) -> list[dict[str, int]]:
    chars = dict(filter(lambda c: c[0].isalpha(), chars.items()))

    return chars
