def triangle_type(a, b, c):
    # Check for a valid triangle first
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"

    # Check for types
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Example usage
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

print("Triangle type:", triangle_type(side1, side2, side3)
