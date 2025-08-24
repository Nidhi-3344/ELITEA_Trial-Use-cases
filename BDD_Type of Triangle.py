# BDD_Type of Triangle.py

from behave import given, when, then
from Type_of_triangle import triangle_type

@given('the triangle sides are {side1:g}, {side2:g}, and {side3:g}')
def step_given_triangle_sides(context, side1, side2, side3):
    context.side1 = side1
    context.side2 = side2
    context.side3 = side3

@when('I check the triangle type')
def step_when_check_triangle_type(context):
    context.result = triangle_type(context.side1, context.side2, context.side3)

@then('the result should be "{expected}"')
def step_then_check_result(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"

# Feature: Triangle Type Checker
# 
#   Scenario Outline: Determine the type of triangle
#     Given the triangle sides are &lt;side1&gt;, &lt;side2&gt;, and &lt;side3&gt;
#     When I check the triangle type
#     Then the result should be "&lt;expected&gt;"
# 
#     Examples:
#       | side1 | side2 | side3 | expected              |
#       | 5     | 5     | 5     | Equilateral triangle  |
#       | 5     | 5     | 6     | Isosceles triangle    |
#       | 3     | 4     | 5     | Scalene triangle      |
#       | 1     | 1     | 3     | Not a valid triangle  |
#       | 0     | 4     | 5     | Not a valid triangle  |
#       | -1    | 4     | 5     | Not a valid triangle  |

# Note: To run these tests, you need to:
# 1. Install behave: pip install behave
# 2. Create a features directory and move this file into it
# 3. Rename this file to triangle_type.feature
# 4. Create a steps directory inside the features directory
# 5. Create a file steps/triangle_steps.py with the step definitions
# 6. Run behave in the parent directory of 'features'