# done
def compute_intersection(rect1, rect2):
    x1 = max(rect1[0], rect2[0])
    y1 = max(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = min(rect1[3], rect2[3])
    
    if x1 < x2 and y1 < y2:
        return [x1, y1, x2, y2]
    else:
        return None

def compute_common_area(rectangles):
    common_area = rectangles[0]
    
    for rect in rectangles[1:]:
        common_area = compute_intersection(common_area, rect)
        
        if common_area is None:
            return 0
    
    area = (common_area[2] - common_area[0]) * (common_area[3] - common_area[1])
    return area

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    
    rectangles = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append([x1, y1, x2, y2])
    
    common_area = compute_common_area(rectangles)
    
    print(f"Case #{case}: {common_area}")