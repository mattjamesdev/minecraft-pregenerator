# Unit tests for script.py

from minecraft_pregenerator.script import seconds_to_time


class TestSecondsToTime:
    """
    Unit tests for script.py
    """

    expected_assert_msg = "Expected {}, got {}"
    
    def test_output_1(self):
        test_input = 0
        expected = (0, 0, 0)
        actual = seconds_to_time(test_input)
        assert expected == actual, self.expected_assert_msg.format(expected, actual)

    def test_output_2(self):
        test_input = 10
        expected = (0, 0, 10)
        actual = seconds_to_time(test_input)
        assert expected == actual, self.expected_assert_msg.format(expected, actual)

    def test_output_3(self):
        test_input = 60
        expected = (0, 1, 0)
        actual = seconds_to_time(test_input)
        assert expected == actual, self.expected_assert_msg.format(expected, actual)

    def test_output_4(self):
        test_input = 3600
        expected = (1, 0, 0)
        actual = seconds_to_time(test_input)
        assert expected == actual, self.expected_assert_msg.format(expected, actual)

    def test_output_5(self):
        test_input = 3661
        expected = (1, 1, 1)
        actual = seconds_to_time(test_input)
        assert expected == actual, self.expected_assert_msg.format(expected, actual)

