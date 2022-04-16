# import shape
import shape as s

print(s.get_box_area(4, -4, 3))
box1 = s.get_box_area(width=4, length=4, height=2)
print('box area:', box1)

circle_area = s.get_circle_area(10)
print('circle area:', circle_area)

triangle_area = s.get_triangle_area(10, 5)
print('triangle area:', triangle_area)