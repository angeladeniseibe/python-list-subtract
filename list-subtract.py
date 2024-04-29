number_input = input("Enter numbers separated by commas: ")
numbers_list = number_input.split(",")

valid_input = True

num_result = None

try:
    num_result = int(numbers_list[0].strip())
    for num_str in numbers_list[1:]:
        num = int(num_str.strip())
        num_result -= num
except ValueError:
    print("Invalid input. Please input numbers only.")
    valid_input = False

if valid_input:
    print("Result:", num_result)
