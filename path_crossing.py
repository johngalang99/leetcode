def isPathCrossing(path):
    points = set()
    x, y = 0, 0
    for c in path:
        points.add((x, y))
        if c == "N":
            y += 1
        if c == "E":
            x += 1
        if c == "S":
            y -= 1
        if c == "W":
            x -= 1

        if (x, y) in points:
            return True

    return False

print(isPathCrossing("NES"))
print(isPathCrossing("NESWW"))

