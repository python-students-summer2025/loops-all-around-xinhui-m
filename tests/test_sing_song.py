import pytest
import string


class Tests:
    def test_for_loop_version_output(self, capsys, monkeypatch):
        """
        Checks whether the output is correct using a for loop.
        """

        from for_loop_version import sing

        # run the function
        sing(5)

        # expected output
        expected = """
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
    """.strip()

        # get the output
        captured = capsys.readouterr()  # capture print output
        actual = captured.out.lower().strip()  # remove leading/trailing whitespace

        # remove multiple whitespaces
        actual = " ".join(actual.split()).strip()
        expected = " ".join(expected.split()).strip()

        # remove all punctuation
        actual = actual.translate(str.maketrans("", "", string.punctuation))
        expected = expected.translate(str.maketrans("", "", string.punctuation))

        # convert to lowercase
        actual = actual.lower()
        expected = expected.lower()

        # make sure the program only asked for input until a valid one was given
        assert actual.lower() == expected.lower()

    def test_for_loop_version_range(self, capsys, monkeypatch):
        """
        Checks whether the for loop version calls the range function
        """

        from for_loop_version import sing

        range_data = {
            "calls": 0,
        }

        # mock the range function
        def new_range(oldrange, *args):
            range_data["calls"] += 1
            if len(args) == 2:
                range = abs(args[1] - args[0])
            elif len(args) == 1:
                range = args[0]
            else:
                range = abs(args[1] - args[0])

            range_data["range"] = range
            return oldrange(*args)

        oldrange = range
        monkeypatch.setattr("builtins.range", lambda *args: new_range(oldrange, *args))

        # run the function
        num_bottles = 10
        sing(num_bottles)

        # check the range function has been called
        assert range_data["calls"] >= 1
        assert (
            range_data["range"] >= num_bottles - 1
        )  # allow for last verse to be outside loop

    def test_while_loop_accumulator_version_output(self, capsys, monkeypatch):
        """
        Checks whether the output is correct using a while loop with accumulator
        """

        from while_loop_accumulator_version import sing

        # run the function
        sing(5)

        # expected output
        expected = """
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
    """.strip()

        # get the output
        captured = capsys.readouterr()  # capture print output
        actual = captured.out.lower().strip()  # remove leading/trailing whitespace

        # remove multiple whitespaces
        actual = " ".join(actual.split()).strip()
        expected = " ".join(expected.split()).strip()

        # remove all punctuation
        actual = actual.translate(str.maketrans("", "", string.punctuation))
        expected = expected.translate(str.maketrans("", "", string.punctuation))

        # convert to lowercase
        actual = actual.lower()
        expected = expected.lower()

        # make sure the program only asked for input until a valid one was given
        assert actual.lower() == expected.lower()

    def test_while_loop_flag_version_output(self, capsys, monkeypatch):
        """
        Checks whether the output is correct using a while loop with flag
        """

        from while_loop_flag_version import sing

        # run the function
        sing(5)

        # expected output
        expected = """
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
    """.strip()

        # get the output
        captured = capsys.readouterr()  # capture print output
        actual = captured.out.lower().strip()  # remove leading/trailing whitespace

        # remove multiple whitespaces
        actual = " ".join(actual.split()).strip()
        expected = " ".join(expected.split()).strip()

        # remove all punctuation
        actual = actual.translate(str.maketrans("", "", string.punctuation))
        expected = expected.translate(str.maketrans("", "", string.punctuation))

        # convert to lowercase
        actual = actual.lower()
        expected = expected.lower()

        # make sure the program only asked for input until a valid one was given
        assert actual.lower() == expected.lower()
