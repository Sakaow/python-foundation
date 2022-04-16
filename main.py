# Evaluate Expression
numbers_list = [3, 1, 5]

def addition(nums: list):
    result = 0
    for i in range(3):
        result += nums[i]
    return result

print(addition(numbers_list))   # 3+1+5 = 9

# addition number in sequence
def addition2(num):
    return num * (num + 1) / 2

print(addition2(5))     # 5*(6/2) = 15.0 = 1+2+3+4+5

def decision():
    for i in range(1, 5):
        print(i)
        if i > 2:
            print('Bigger than 2')
        print('Done with i', i)
    print('All done!')

#decision()  # call the function

def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0
    return width * length * height

print(get_box_area(4, -4, 3))
box1 = get_box_area(width=4, length=4, height=2)
print(box1)
