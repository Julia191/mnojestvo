def distance(x1, y1, x2, y2):
    x1_x2 = (x1 - x2)
    x1_x2_2 = (x1_x2 ** 2)
    y1_y2 = (y1 - y2)
    y1_y2_2 = y1_y2 ** 2
    res = (x1_x2_2 + y1_y2_2) ** 0.5
    return res


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


print(distance(x1, y1, x2, y2))
