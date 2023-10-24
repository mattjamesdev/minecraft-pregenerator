# Command line interface for entering custom values for coordinates.

from minecraft_pregenerator.script import confirm_and_run


def validate_input(prompt: str, default: int, err: str = "Invalid input") -> int:
    """
    Get integer input from the user. If input cannot be converted to an integer,
    ask the user for input again. If no input is entered, return a default value.

    Parameters
    ----------
    prompt : str
        Input prompt to display.
    default : int
        Default value to use if no input is entered.
    err : str
        Message to display when input is invalid. Default "Invalid input".

    Return
    ------
    int
        The user's valid input.
    """
    # Get input until the input is valid
    while True:
        user_input = input(prompt)
        if user_input == "":
            return default
        try:
            return int(user_input)
        except ValueError:
            print(err)


def main():
    """
    Run the interactive interface, allowing the user to input custom values for
    the parameters.
    """
    welcome_text = (
        "Welcome to Minecraft World Pre-generator! This script will generate a series of\n"
        "/tp commands and automatically enter them for you. Make sure you have Minecraft\n"
        "running in the world you want to pre-generate before you activate this script.\n"
    )
    print(welcome_text)

    # Get x-range, checking that the first is less than the second
    while True:
        x_min = validate_input("Enter a minimum x-coordinate (default -2880): ", -2880)
        x_max = validate_input("Enter a maximum x-coordinate (default 2880): ", 2880)
        if x_min < x_max:
            break
        else:
            print("Maximum must be greater than minimum.")

    # Get z-range, checking that the first is less than the second
    while True:
        z_min = validate_input("Enter a minimum z-coordinate (default -2880): ", -2880)
        z_max = validate_input("Enter a maximum z-coordinate (default 2880): ", 2880)
        if z_min < z_max:
            break
        else:
            print("Maximum must be greater than minimum.")

    # Get y-coordinate, checking that it is greater than 0
    while True:
        height = validate_input(
            "Enter a height (y-value) greater than 0 (default 192): ", 192
        )
        if height > 0:
            break
        else:
            print("Height must be greater than 0.")

    # Get the step size, checking that it is positive.
    while True:
        step_size = validate_input(
            "Enter a teleport step size, the distance between teleports in blocks (default 240): ",
            240,
        )
        if step_size > 0:
            break
        else:
            print("Teleport step size must be a positive whole number.")

    while True:
        delay = validate_input(
            "Enter a time (in seconds) to wait between teleports in seconds (default 2): ",
            2,
        )
        if delay > 0:
            break
        else:
            print("Delay must be greater than 0 seconds.")
    print()

    # Run the commands
    confirm_and_run(x_min, x_max, z_min, z_max, height, step_size, delay)

