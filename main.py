"""
Sings the class American song, "99 Bottles of Beer on the Wall" in three different styles.
- one using a for loop
- one using a while loop controlled by an accumulator
- another using a while loop controlled by a flag
"""

# import the three different versions using aliases to keep the names shorter
import for_loop_version as flv
import while_loop_accumulator_version as wlav
import while_loop_flag_version as wlfv


def main():
    """
    Runs each of the three versions of the program. For each, we...
    - calls the get_starting_number function to determine how many bottles of beer to start with.
    - and then call the sing method, passing the number of bottles to start as its argument.
    """

    # run for loop version
    num_bottles = flv.get_starting_number()
    flv.sing(num_bottles)

    # run while loop with accumulator version
    num_bottles = wlav.get_starting_number()
    wlav.sing(num_bottles)

    # run while loop with flag version
    num_bottles = wlfv.get_starting_number()
    wlfv.sing(num_bottles)


# call main
main()
