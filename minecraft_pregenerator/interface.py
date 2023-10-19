# Command line interface for entering custom values for coordinates.
from script import main

welcome_text = """\
Welcome to Minecraft World Pre-generator! This script will generate a series of 
/tp commands and automatically enter them for you. Make sure you have Minecraft 
running in the world you want to pre-generate before you activate this script. \n"""


def interface():
    print(welcome_text)
    while True:
        try:
            # Get the coordinates and values from user input.
            # If there is no input, set it to the default value.
            # For the coordinates, check that the min is less than the max.
            xmin_input = input("Enter a minimum x-coordinate (default -2880): ")
            xmin = int(xmin_input) if xmin_input else -2880
            xmax_input = input("Enter a maximum x-coordinate (default 2880): ")
            xmax = int(xmax_input) if xmax_input else 2880
            if xmax <= xmin:
                print("Maximum must be greater than minimum.")
                continue
            zmin_input = input("Enter a minimum z-coordinate (default -2880): ")
            zmin = int(zmin_input) if zmin_input else -2880
            zmax_input = input("Enter a maximum z-coordinate (default 2880): ")
            zmax = int(zmax_input) if zmax_input else 2880
            if zmax <= zmin:
                print("Maximum must be greater than minimum.")
                continue

            height_input = input(
                "Enter a height (y-value) greater than 0 (default 192): "
            )
            height = int(height_input) if height_input else 192
            if height <= 0:
                print("Height must be greater than 0.")
                continue

            # When getting the step size, also check that it is positive.
            while True:
                step_size_input = input(
                    "Enter a teleport step size, the distance between teleports in blocks \n(default 240): "
                )
                step_size = int(step_size_input) if step_size_input else 240
                if step_size <= 0:
                    print("Teleport step size must be a positive whole number.")
                    continue
                break

            delay_input = input(
                "Enter a time to wait between teleports in seconds (default 2): "
            )
            delay = int(delay_input) if delay_input else 2
            print()
            break
        except ValueError:
            print("Invalid input: please enter a whole number.")
            print()
            continue

    main(xmin, xmax, zmin, zmax, height, step_size, delay)


if __name__ == "__main__":
    interface()
