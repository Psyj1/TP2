option = int(input("\n 1 - Cash \n 2 - Extract \n 3 - Exit \n Choose an option: "))

match option:
    case 1:
        print("You choose the cash option")
        val = float(input("Type an value to cash: $: "))
        print(f"Cashing to your account the value of {val}...")
    case 2:
        print("Choose the option Extract")
    case 3:
        exit
    case _:
        print("Invalid option")            