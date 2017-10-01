total_input = input("Please enter something: ")
print("you entered", total_input)

total_input = int(total_input)
for i in range(0, total_input):
    input_value = input();
    numbers = input_value.split(' ');
    print(numbers)
    # print(numbers[0])
    if len(numbers) >= 2:
        if numbers[0] > numbers[1]:
            print(">", numbers)
        elif numbers[0] < numbers[1]:
            print("<")
        else:
            print("=")
