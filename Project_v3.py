import math

SP_CHAR = "!@#$%^&*()_+-=[]{}|;':\",.<>?/`~ "


def calc_entropy(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SP_CHAR:
            has_symbol = True

    R = 0
    if has_upper:
        R += 26
    if has_lower:
        R += 26
    if has_digit:
        R += 10
    if has_symbol:
        R += len(SP_CHAR)

    L = len(password)
    entropy = L * math.log2(R)
    return entropy, has_upper, has_lower, has_digit, has_symbol


def check_password(password, entropy, has_upper, has_lower, has_digit, has_symbol):

    L = len(password)
    sentence = ""

    if entropy < 35:
        print("Password is too weak")
        if L < 8:
            sentence += "Try adding more characters"
        if not has_upper:
            sentence += (", Mix in more uppercase letters")
        if not has_lower:
            sentence += (", Mix in more lowercase letters")
        if not has_digit:
            sentence += (", Include more digits")
        if not has_symbol:
            sentence += (", Include more symbols")
        print(f"{sentence}.")

    else:
        print("Password strength is OK.")


def main():
    password = input("Enter the password: ")
    try:
        entropy, has_upper, has_lower, has_digit, has_symbol = calc_entropy(password)
        print(f"Entropy: {entropy:.2f} bits")
        check_password(password, entropy, has_upper, has_lower, has_digit, has_symbol)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
