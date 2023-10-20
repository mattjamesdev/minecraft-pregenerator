# Unit tests for script.py

import pytest

from minecraft_pregenerator.script import seconds_to_time


class TestSecondsToTime:
    """
    Unit tests for seconds_to_time
    """

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (0, (0, 0, 0)),
            (10, (0, 0, 10)),
            (60, (0, 1, 0)),
            (3600, (1, 0, 0)),
            (3661, (1, 1, 1)),
        ]
    )
    def test_output(self, test_input, expected):
        """
        Test output value.
        """
        actual = seconds_to_time(test_input)
        assert expected == actual, f"Expected {expected}, got {actual}"

