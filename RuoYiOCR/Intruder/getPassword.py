def getPassword():
    with open("./password.txt") as f:
        lines = [line.strip() for line in f]
    f.close()
    return set(lines)