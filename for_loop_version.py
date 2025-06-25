def get_starting_number():
    '''
    ask the user how many bottles of beer on the wall they want to start singing with
    '''
    while True:
        bottle_num = input("How many bottles of beer on the wall? ")
        if bottle_num.isnumeric() and int(bottle_num) >= 1:
            return int(bottle_num)

def sing(num_bottles):
    for bottle in range(num_bottles, 1, -1):
        if bottle > 2:
            print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer.\nTake one down, pass it around, {bottle -1} bottles of beer on the wall.")
        elif bottle == 2:
            print(f"{bottle} bottles of beer on the wall, {bottle} bottles of beer.\nTake one down, pass it around, {bottle-1} bottle of beer on the wall.")
    
    print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        
