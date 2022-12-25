'''A private bank has a problem with its credit card processing system. As a result, the majority of customers 
have contacted the bank about the payment problem. Now the bank has to check whether the credit number is 
valid or not before proceeding with the further clearance process. Write a program to obtain a credit card 
number and check its validity. Card numbers should start with 4 for Visa cards, 5 for Master cards, 37 for
American Express cards, and 6 for Discover cards. Conditions for a card to be valid: Consider the card 
number: 4388576018402626 Step 1: Double every second digit from right to left. If doubling of a digit 
results in a two-digit number, add up the two digits to get a single-digit number 
(like for 12: 1 + 2, 18: 1 + 8). Step 2: Add all of the single-digit numbers from 
Step 1. (4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37) 
Step 3: Add all the digits in the odd places from right to left in the card number. 
(6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38) Step 4: Sum the results from Steps 2 and 3. (37 + 38 = 75) 
Step 5: If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid.'''
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card #: ")

card_number = card_number[::-1]

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")                   
