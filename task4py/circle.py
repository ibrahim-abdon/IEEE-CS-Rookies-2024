# Done
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def do_circles_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    radius_a = calculate_distance(x1, y1, x2, y2) / 2
    radius_b = calculate_distance(x3, y3, x4, y4) / 2

    center_a = ((x1 + x2) / 2, (y1 + y2) / 2)
    center_b = ((x3 + x4) / 2, (y3 + y4) / 2)

    distance_centers = calculate_distance(center_a[0], center_a[1], center_b[0], center_b[1])

    return "YES" if distance_centers <= (radius_a + radius_b) else "NO"

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

result = do_circles_intersect(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)
