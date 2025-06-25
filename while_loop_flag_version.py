def get_starting_number():
    '''
    ask the user how many bottles of beer on the wall they want to start singing with
    '''
    while True:
        bottle_num = input("How many bottles of beer on the wall? ")
        if bottle_num.isnumeric() and int(bottle_num) >= 1:
            return int(bottle_num)

def sing(num_bottles):
    keep_singing = True
    while keep_singing:
        if num_bottles > 1:
            next_num = num_bottles -1
            if next_num == 1:
                next_word = "bottle"
            else:
                next_word = "bottles"
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.\nTake one down, pass it around, {next_num} {next_word} of beer on the wall.")
            num_bottles = num_bottles -1
            
        elif num_bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
            keep_singing = False

