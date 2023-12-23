def isPathCrossing(path):
    points = {(0,0): 1}
    x, y = 0, 0
    for c in path:
        if c == "N":
            y += 1
        if c == "E":
            x += 1
        if c == "S":
            y -= 1
        if c == "W":
            x -= 1
        points[(x, y)] = 1 + points.get((x,y), 0)

    print(points)
    has_value_greater_than_2 = any(value >= 2 for value in points.values())
    print(has_value_greater_than_2)
    if has_value_greater_than_2:
          return True
    else:
        return False

isPathCrossing("NES")
isPathCrossing("NESWW")

