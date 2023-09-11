# pylint: disable=missing-module-docstring
def calculate_average(numbers):
    """function for calculate average value"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
RESULT = calculate_average(nums)
print("The average is:", RESULT)
