'''

Lab 6
Authors: Trent Ford and Thurston Ngo
Class:COP3502
Section: 22282
Description: Encoder and decoder by taking number and adding or subtracting 3 to each digit

'''

def encode(password):
    encodedPassword = ""
    for num in password:
        if num.isdigit() and int(num) <= 6:
            encodedPassword += str(int(num) + 3)
        elif int(num) == 7:
            encodedPassword += "0"
        elif int(num) == 8:
            encodedPassword += "1"
        elif int(num) == 9:
            encodedPassword += "2"
    return encodedPassword


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        num = int(digit)
        if num == 0:
            decoded_password += "7"
        elif num == 1:
            decoded_password += "8"
        elif num == 2:
            decoded_password += "9"
        else:
            decoded_password += str(num - 3)
    return decoded_password


def main():
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit \n")
        userInput = int(input("Please enter an option: "))

        if userInput == 1:
            stringToEncode = input("Please enter your password to encode: ")
            if len(stringToEncode) == 8:
                encodedPassword = encode(stringToEncode)
                print("Your password has been encoded and stored!")

        if userInput == 2:
            print(f"The encoded password is {encodedPassword}, and the original password is {decode(encodedPassword)}.")

        if userInput == 3:
            break


if __name__ == '__main__':
    main()