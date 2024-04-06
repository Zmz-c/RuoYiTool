
def getUsername():
    with open("./username.txt") as f:
        lines = [line.strip() for line in f]
    f.close()
    return set(lines)
