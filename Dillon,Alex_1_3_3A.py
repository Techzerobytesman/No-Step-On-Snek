
a = 3
a**2

a+1 >= 2 and a**2 !=5

def age_limit_output(age):
    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print(age, "is below the age limit.")
    else:
        print(age, "is old enough.")
    print("Minimum age is", AGE_LIMIT)

def report_grade(percent):
    if percent >= 80:
        print("A grade of", percent, "does not indicate mastery. Get gud.")
    else:
        print("A grade of", percent, "Indicates mastery. Good job.")

def vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        print("True")
    else:
        print("False")

def letter_in_word(guess, word):
    if guess in word:
        print ("True")
    else:
        print ("False")

def hint(color, secret):
    if color in secret:
        print ("The color", color, "is in the sequence of colors")
    else:
        print ("The color", color, "is not in the sequence of colors")