from art import art
from morse import MorseCode
from sound import transmit

print(art)

morse_code = MorseCode()

while True:
    operation = input("Do you wish to Encode or Decode? (e for EXIT)\n").lower()

    if operation == "e":
        break

    elif operation == 'encode':
        text = input("Enter your text here: \n")
        try:
            code = morse_code.encode(text)
            print("Your Morse Code is: {}".format(code), end='\n')
            sound = input("Do you want to hear your code sound? y:yes, n:no : ").lower()
            if sound == "y":
                transmit(code=code)

        except KeyError:
            print(text)
            print("Your text must only contains alphabets and digit numbers.")

    elif operation == 'decode':
        try:
            text = morse_code.decode()
            print("Your message is: {}".format(text, end='\n'))
        except KeyError:
            print(
                """
                    Type morse code using '.', '-', 
                    using a spaces between letters and
                    '/' between words.
                """
            )
    else:
        print("OOPS! You have an typo error, make sure to write it right.")
    



