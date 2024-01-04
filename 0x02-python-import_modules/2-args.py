#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    count = len(sys.argv) -1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
    else:
        print("{} arguments".format(count))
    if count >= 1:
        count = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
