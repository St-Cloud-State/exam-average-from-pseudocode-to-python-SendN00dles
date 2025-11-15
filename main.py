"""
Full Name: Ryan Serbus
Class-Section: IS 250-01
Assignment Title: Calculate Average of Three Scores
Submission Date: 11/17/2025
"""
"""
Pseudo Code: 
Ask the user for three scores
"What is score 1: "
"What is score 2: "
"What is score 3: "
Print each score to show the user
"You entered these scores: "
"score 1: "
"score 2: "
"score 3: "
Find the average of three scores
"The average score is: "
First Commit
"""
#define function for average scores
def calculate_average(one, two, three):

#return the average
    return (one + two + three) / 3

#define main
def main ():

#ask for first score
    one = float(input("What is score 1: "))

#ask for second score
    two = float(input("What is score 2: "))

#ask for third score
    three = float(input("What is score 3: "))

#confirm the scores:
    print("You have entered these scores:")

#print the first score
    print("Score 1:",one)

#print the second score
    print("Score 2:",two)

#print the third score
    print("Score 3:",three)

#call calculate_average function
    average = calculate_average(one, two, three)

#print the average score
    print(f"The average score is: {average:.2f}")

#call main
main()

#second commit
  
