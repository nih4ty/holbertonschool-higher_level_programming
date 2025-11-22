#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    for arg in sys.argv[1:]:   # argv[0] fayl adıdır, qalanlar arqumentlərdir
        total += int(arg)

    print(total)
