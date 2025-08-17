def classify_triangle(s1, s2, s3):
    """
    Classifies a triangle based on its side lengths.

    Args:
        s1 (float): Length of the first side.
        s2 (float): Length of the second side.
        s3 (float): Length of the third side.

    Returns:
        str: "Equilateral Triangle", "Isosceles Triangle", "Scalene Triangle",
             or "Not a Triangle".
    """
    # Check triangle inequality theorem
    if not (s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
        return "Not a Triangle"
    
    # Classify the triangle type
    if s1 == s2 == s3:
        return "Equilateral Triangle"
    elif s1 == s2 or s1 == s3 or s2 == s3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

# Get input from the user
try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Ensure side lengths are positive
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Side lengths must be positive numbers.")
    else:
        result = classify_triangle(side1, side2, side3)
        print(f"The given sides form a: {result}")

except ValueError:
    print("Invalid input. Please enter numeric values for side lengths.")