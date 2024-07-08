import random
import string
def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passcode = ''.join(random.choice(characters) for i in range(length))
    return passcode
def main():
    try:
        desired_length = int(input("Enter the length of password : "))
        if desired_length <= 0:
            print("Length of password cannot be less than zero")
            return
        passcode = password(desired_length)
        print("Generated Password : ",passcode)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
main()