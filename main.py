# Source Code: Trentyne Morgan
# Version 1.2 - September 18, 2020 - (Revised on August 13, 2021)

# Define Variables - (Leave Uninitilized and make global to all of the application)
# Ordered Pair 1 = (pair_1a, pair_1b)
# Ordered Pair 2 = (pair_2a, pair_2b)
orderedPair1 = [0, 0]
orderedPair2 = [0, 0]
pair_1a = 0
pair_1b = 0
pair_2a = 0
pair_2b = 0

# The result of subtracting both the X and Y axis together in both of the ordered pairs
pair_sum_1 = 0
pair_sum_2 = 0

# The result of multiplying the exponents go in here
pair_square_sum_1 = 0
pair_square_sum_2 = 0

# Adding both of the sums together 
square_result = None

# Program Title
def Program_Title():
   # Program Title/Start Message
   print("Distance Formula Calculator (Version 1.2)\nWeb App by: Trentyne Morgan\n\nBug Reporting: trentynemorgan@outlook.com\n\n")

   # Prompt user for entering ordered pairs
   Ordered_Pair_Entry()

# Entering Ordered Pairs
def Ordered_Pair_Entry():
   # Global Variables
   global pair_1a
   global pair_1b
   global pair_2a
   global pair_2b
   global orderedPair1
   global orderedPair2

   # Get Ordered Pairs from User Input
   orderedPair1[0] = input("Enter the first digit in the first ordered pair: ")
   orderedPair1[1] = input("Enter the second digit in the first ordered pair: ")
   print("\n")
   orderedPair2[0] = input("Enter the first digit in the second ordered pair: ")
   orderedPair2[1] = input("Enter the second digit in the second ordered pair: ")

   # Subtract the Ordered Pairs
   Subtract_Pairs()

# Subtract the Ordered Pairs 
def Subtract_Pairs():
   global pair_sum_1
   global pair_sum_2

   # Convert str to type int (string literal -> integer)
   pair_sum_1 = int(orderedPair1[0]) - int(orderedPair1[1])
   pair_sum_2 = int(orderedPair2[0]) - int(orderedPair2[1])

   # Square the Pairs (Times it by itself)
   Square_Pairs()
   
# Square Pairs - (Times it by itself)
def Square_Pairs(): 
   global pair_square_sum_1
   global pair_square_sum_2

   # Convert str to type int (string literal -> integer)
   pair_square_sum_1 = int(pair_sum_1) * int(pair_sum_1)
   pair_square_sum_2 = int(pair_sum_2) * int(pair_sum_2)
   Square_Result_Add()
   
# Add the results from the Square_Pairs function
def Square_Result_Add():
   global square_result
   square_result = int(pair_square_sum_1) + int(pair_square_sum_2)
   Show_Result()

# Print Result
def Show_Result():
   print("\nThe distance is: ")
   print(square_result)
   Restart_Application_Prompt()
   
# Restart Application if the user needs to
def Restart_Application_Prompt():
   print("\n\nDo another?\n\n1.) Yes\n2.) No\n")
   repeat_option = input("Type the number of the choice you wish to pick: ")
   # Check the users option
   if repeat_option == "1":
     print("\n\n")
     Ordered_Pair_Entry()
   if repeat_option == "2":
     print("\n\nThank you for using my distance formula calculator!")
     # Exit Application
     quit()
   else:
       print("\n\nInvalid Choice. Please Try Again")
       Restart_Application_Prompt()

Program_Title()