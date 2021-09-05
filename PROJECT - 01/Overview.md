# Milestone Project 1 - Tik Tak Toe
***
***
# Warm-up / Info
### Standard Workflow
* visual representation
* user input
* function 
* updates
* new visual
* updated visual

## Displaying Information
```
def display (row1,row2,row3)
    print(row1)
    print(row2)
    print(row3)

display([1,2,3])
```
```
def display (row1,row2,row3)
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 - [' ',' ',' ']

display(row1,row2,row3)

# to change one of the values in the list: 
row2[1] = 'X' 
```
## Accepting User Input
* Get input
```
result = int(input("Please enter a number:"))
type(result)
```
```
position_index = int(input("choose an index positions:"))

row1[position_index]
```
## Validating User Input
* you should validate user input to avoid errors or invalid conversions
* **without validation:**
```
def user_choice():
     choice = input(please enter a number (0-10): ")

     return int(choice)
```
* **with validation:**
* confirm it can be converted to an int
```
some_value = '100'
some_value.isdigit()
int(some_value)
```
```
def user_choice():
    # VARIABLES

    #inital
     choice = 'Wrong'
     acceptable_range = range(1,10)
     within_range = False

     while choice.isdigit() == False or within_range==False:
          choice = input(please enter a number (0-10): ")
          # Digit check
          if choice.isdigit() == False:
             print("Sorry that is not a digit")
          # Range check
          if choice.isdigit() == True:
             if int(choice) in acceptable_range:
                   within_range = True
          else: 
              print("you are outside of the acceptable range")
              within_range = False
         
     return int(choice)

user_choice()
```
## Simple User Interaction
* **Objective:**
* display a list
* have a user choose an index position and an input value
* replace value at index position with users chosen input value

* display function:
```
game_list - [0,1,2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)
```
* get position choice:
```
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice! ")
    return(int(choice))
```
* choose a replacement value
```
def replacement_choice(game_list,position_choice):
     user_placement = input("Type a string to place at position: ")
     game_list[position] = user_placement

     return game_list
```
* code that keeps the game going - or gives the option to quit
```
def game_on():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Keep Playing (Y or N): ")
        if choice not in ['Y','N']:
            print("Sorry, I dont understand, please choose Y or N ")
    if choice == "Y":
       return True
    else: 
       return False
```
* putting it all together
```
game_on = Ture
game_list - [0,1,2]

while game_on == True:
   display_game(gamelist)
   position = position_choice()
   game_list = replacement_choice(game_list,position)
   display_game(gamelist)
   game_on = gameon_choice()
```
