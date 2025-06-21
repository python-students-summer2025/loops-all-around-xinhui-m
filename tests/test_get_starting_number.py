import pytest

from for_loop_version import *


class Tests:
    def mock_input(self, mock_data, call_counter, monkeypatch):
        """
        Mock the builtin input function
        :param mock_data: Dictionary of data to mock.
        :param call_counter: Dictionary of counters for function calls
        :param monkeypatch: pytest's monkeypatch object
        """

        # mock the input function
        def new_input(message):
            call_counter["input"] += 1
            return mock_data["input"].pop(0)

        monkeypatch.setattr("builtins.input", lambda x: new_input(x))

    def test_get_starting_number(self, monkeypatch):
        """
        Checks whether we keep asking until the user enters a valid starting number
        """

        mock_data = {"input": ["foo", "bar", "0", "3", "1", "100"]}
        call_counter = {
            "input": 0,
        }
        # mock the input function
        self.mock_input(mock_data, call_counter, monkeypatch)

        # run the function
        get_starting_number()

        # make sure the program only asked for input until a valid one was given
        assert call_counter["input"] == 4
