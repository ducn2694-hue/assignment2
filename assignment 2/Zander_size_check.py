def check_zander_size():
    size_limit = 42
    length = float(input("Enter the length of the zander (cm): "))

    if length < size_limit:
        difference = size_limit - length
        print(f"Release the fish back into the lake.")
        print(f"It was {difference:.2f} cm below the size limit.")
    else:
        print("The zander meets the size limit.")
check_zander_size()
