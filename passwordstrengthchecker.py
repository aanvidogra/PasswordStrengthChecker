import string

password= input("Enter the password: ")

upper_case = any(c in string.ascii_uppercase for c in password)
lower_case = any(c in string.ascii_lowercase for c in password)
digits = any(c in string.digits for c in password)
special = any(c in string.punctuation for c in password)

characters= [upper_case, lower_case, digits, special]

length= len(password)

score = 0

with open('commonpasswords.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found on the common list. Score 0/7")
    exit()

if length > 8:
    score+=1
if length > 12:
    score+=1
if length > 17:
    score+=1
if length > 25:
    score+=1
print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score+=1
if sum(characters) > 2:
    score+=1
if sum(characters) > 3:
    score+=1
print (f"Password has {str(sum(characters))} different character types, adding {str(sum(characters)-1)} points!")


if score < 4:
    print(f"The password is weak! Score: {str(score)} / 7")
elif score == 4:
        print(f"The password is ok! Score: {str(score)} / 7")
elif 4 < score < 6:
        print(f"The password is pretty good! Score: {str(score)} / 7")
elif score > 6:
        print(f"The password is excellent! Score: {str(score)} / 7")
