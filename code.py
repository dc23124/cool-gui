def code():
    while True:
        name = input("input your name: ") 
        if name.isalpha():
            break
        print("Invalid input. Please do not use numbers, spaces, or symbols.")
        print(f"Your name is {name}!")

        age = int(input("input your age: "))
        if age < 12: 
            print("ERROR")
            break
        else:
            continue