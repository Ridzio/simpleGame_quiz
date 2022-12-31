print ("Welcome to the Quiz Game!")

score = 0

#Question 1
print ("Q1: What is 4+2?")
answer = input("Your answer: ")

if answer == "6":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

#Question 2
print ("Q2: What is 7-3?")
answer = input("Your answer: ")

if answer == "4":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

#Question 3
print ("Q3: What is 8*2?")
answer = input("Your answer: ")

if answer == "16":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

print ("You got", score, "out of 3 questions correct!")