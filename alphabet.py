user_input = input("Enter a character:")

if len(user_input) == 1:
    if user_input.isalpha():
        print(f"'{user_input}' is an alphabet.")
    else:
        print(f"'{user_input}' is not an alphabet.")
else:
    print("Please enter only a single character.")
