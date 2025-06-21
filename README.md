## 99 Bottles of Beer (A Traditional American Song)

Welcome! Your assignment is to write a program that sings (i.e. prints) the road trip song, "99 Bottles of Beer".

To quote ,

> "99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. In particular the song is frequently sung by children on long bus trips, such as class field trips, or on Scout and/or Girl Guide outings.
>
> -[Wikipedia](http://en.wikipedia.org/wiki/99_Bottles_of_Beer)

Depending on how long the road trip is, students (i.e. users), must decide how many bottles of beer to start with. So the program should ask for that input. The program should then proceed to output lyrics from the song until there are no more bottles of beer on the wall.

## Example input/output

Sample input (with example student response):

```
How many bottles of beer on the wall? 5
```

Sample output:

```
5 bottles of beer on the wall, 5 bottles of beer.
Take one down, pass it around, 4 bottles of beer on the wall.

4 bottles of beer on the wall, 4 bottles of beer.
Take one down, pass it around, 3 bottles of beer on the wall.

3 bottles of beer on the wall, 3 bottles of beer.
Take one down, pass it around, 2 bottles of beer on the wall.

2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall!
```

## Requirements

### Create three versions of the singing algorithm

Create three different versions of the program that each ask the user to enter the number of starting bottles and output the lyrics, but are executed in different styles:

1. one version that uses a for loop, saved in a file named `for_loop_version.py`.
1. another version that uses a while loop controlled by an accumulator variable, saved in a file named `while_loop_accumulator_version.py`
1. yet another version that uses a while loop controlled by a flag, saved in a file named `while_loop_flag_version.py`. You are welcome to use other patterns in this version as long as the flag variable is used directly to determine whether the loop should continue iterating or terminate.

Each version (and thus each file) must include two functions:

- `get_starting_number` - this function asks the user how many bottles of beer on the wall they want to start singing with, e.g. "How many bottles of beer on the wall?" The function asks this question as many times as necessary until the user enters a valid response, which is considered to be any integer 1 or greater. The function then returns the integer equivalent of the value the user entered. The code for this function can be the same for all three versions of the program, but must be copied into each file.
- `sing` - this function takes an argument specifying how many bottles of beer to start with, and then outputs the lyrics to the song, starting from that number of bottles.

### A main program file.

A file named `main.py` is the main entry point for running the program. This contains a `main` function that runs each of the three different versions of the program.

- The code in this file is given to you.
- Run this main file to test your program.

### Output the correct lyrics

Be attentive to detail:

- "One bottle" is singular, while "Two bottles" is plural. This grammar must be correctly output by your program.
- The last verse says, "no more bottles of beer on the wall!" instead of "0 bottles of beer on the wall."

Your program must not output anything except the initial question to the user (asked once), and then the song lyrics output by each of the three functions.

## Debugging

### Verify the output is correct

One of the easiest ways to debug a program simply to verify that it behaves correctly when you run it. Try running it with a variety of valid and invaalid inputs to be sure it behaves according to instructions under all circumstances.

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. If the functions have been completed correctly, all tests should pass. You should not edit any files in the `test` directory.

If the tests do not appear, or seem to never stop loading, open up a Terminal window and run the command, `pytest --collect-only`, to see whether there are any errors in the code that prevent the tests from being discovered.

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
