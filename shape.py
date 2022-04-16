def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0
    return width * length * height

def get_circle_area(radius):
    return 22/7 * (radius ** 2)

def get_triangle_area(base, height):
    return 1/2 * base * height

def get_rectangle_area(width, height):
    return width * height

