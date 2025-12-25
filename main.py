import random
import string
import pyautogui
import pyperclip

# Ask user for min and max lengths
minimumLength = int(pyautogui.prompt(
    text="Enter the minimum characters in your password.",
    title='Minimum Characters',
    default='5'
))

maximumLength = int(pyautogui.prompt(
    text="Enter the maximum characters in your password.",
    title='Maximum Characters',
    default=str(minimumLength + 5)  # Just a suggestion
))


def passwordEngine(minLength, maxLength):
    length = random.randint(minLength, maxLength)
    possibleCharacters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(possibleCharacters) for i in range(length))

    result = pyautogui.alert(
        text="Your new secure password is:\n" + password,
        title="Password Generated!",
        button="Copy"
    )

    if result == "Copy":
        pyperclip.copy(password)
        pyautogui.alert(
            "Thank you for using PASSWD, the most secure and open-source password generator!",
            title="Thank you",
            button="Exit"
        )


def main():
    passwordEngine(minimumLength, maximumLength)


# Start the program
main()
