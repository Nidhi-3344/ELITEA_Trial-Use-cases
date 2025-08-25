def triangle_type(a, b, c):
    # Check for invalid inputs
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"
    
    # Check if it's a valid triangle
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return "Not a valid triangle"
    
    # Determine the triangle type
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Example usage
if __name__ == '__main__':
    print(triangle_type(5, 5, 5))  # Equilateral triangle
    print(triangle_type(5, 5, 7))  # Isosceles triangle
    print(triangle_type(3, 4, 5))  # Scalene triangle
    print(triangle_type(1, 1, 3))  # Not a valid triangle
    print(triangle_type(0, 1, 1))  # Not a valid triangle
    print(triangle_type(-1, 1, 1))  # Not a valid triangle