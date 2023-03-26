def main():
    user_greeting = input("Dear bank officers, Please greet bank users properly :").lower().title().strip()
    print(user_greeting)
    print(f"${value(user_greeting)}") 


def value(greeting):
    money = 0
    if greeting == "Hello":
        money = 0
        return  money
    elif greeting[0] == "H" and greeting != "Hello":
        money = 20
        return  money
    else:
        money = 100
        return  money


if __name__ == "__main__":
    main()