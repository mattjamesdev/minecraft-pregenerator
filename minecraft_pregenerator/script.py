# minecraft-pregenerator by mattjamesdev
# Inspired by Xisumavoid's video on pre-generating the world for Hermitcraft season 7.
# https://www.youtube.com/watch?v=eA35S2GW-jI

# Command: /tp <targets> <location> [<rotation>]
# e.g. /tp @p 0 100 0 -180.0 0.0
# teleports the player to (x, y, z) = (0, 100, 0), facing North at eye level.

# Rotation directions
# yaw/horizontal:
# -180.0 - North
# -90.0 - East
# 0.0 - South
# 90.0 - West
#
# pitch/vertical:
# -90.0 - straight up
# 0.0 - eye level
# 90.0 - straight down

import time
import platform

import keyboard as kb


def seconds_to_time(seconds: int) -> tuple[int, int, int]:
    """
    Given a duration in seconds, returns the number of hours, minutes, and seconds of
    that duration.

    Parameters
    ----------
    seconds : int
        A time duration in seconds.

    Returns
    -------
    tuple[int, int, int]
        The number of hours, minutes, and seconds.
    """
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)
    return hours, minutes, seconds


def tp_command(location: tuple[int, int, int], yaw: float = -180.0, pitch: float = 20.0) -> str:
    """
    Generate the `/tp` command to write given coordinates, pitch, and yaw.

    Parameters
    ----------
    location : tuple[int, int, int]
        A 3-tuple (x, y, z) of the desired coordinates.
    yaw : float, default -180.0
        Yaw (horizontal direction) to face when teleporting.
    pitch : float, default 20.0
        Pitch (vertical direction) to face when teleporting.

    Returns
    -------
    str
        Formatted teleport command. Example:
        `/tp @p 100 64 200 -180.0 20.0`
    """
    return f'/tp @p {location[0]} {location[1]} {location[2]} {yaw} {pitch}'


# The main bulk of the script.
def execute_commands(x_min: int, x_steps: int, z_min: int, z_steps: int, y_height: int, step_size: int, delay: float) -> None:
    """
    Type out a series of `/tp` commands to teleport the player around.

    Parameters
    ----------
    x_min : int
        Starting x-coordinate.
    x_steps : int
        Number of steps to take in the x-direction.
    z_min : int
        Starting z-coordinate.
    z_steps : int
        Number of steps to take in the z-direction.
    y_height : int
        y-coordinate to teleport to.
    step_size : int
        How far to step in each direction (except y).
    delay : float
        Time in seconds to wait between teleport commands.
    """
    # Grid of teleports
    for z_step in range(z_steps):
        for x_step in range(x_steps):
            coords = (x_min + step_size*x_step, y_height, z_min + step_size*z_step)
            # Face four different directions to generate terrain all around the player
            for n in range(4):
                yaw_angle = -180.0 + n*90
                kb.send('t')  # Open the chat in Minecraft
                time.sleep(0.05)
                kb.write(tp_command(coords, yaw_angle))
                time.sleep(0.05)
                kb.send('enter')
                time.sleep(delay)


def main(x_min: int, x_max: int, z_min: int, z_max: int, height: int, step_size: int, delay: float) -> None:
    """
    Run the execution script. The main purpose of this function (instead of just using
    `execute_commands`) is to provide the user some info before actually starting the
    script. It also asks the user for confirmation before beginning to type.

    Parameters
    ----------
    x_min : int
        Starting x-coordinate.
    x_steps : int
        Number of steps to take in the x-direction.
    z_min : int
        Starting z-coordinate.
    z_steps : int
        Number of steps to take in the z-direction.
    height : int
        y-coordinate to teleport to.
    step_size : int
        How far to step in each direction (except y).
    delay : float
        Time in seconds to wait between teleport commands.
    """
    x_no_steps = int((x_max - x_min)/step_size) + 1
    z_no_steps = int((z_max - z_min)/step_size) + 1
    no_of_tps = x_no_steps*z_no_steps

    # Approximate the time it will take to run.
    # If running on macOS, there is a short delay between typing each character, 
    # whereas on Windows the commands are typed out almost instantly. The 
    # "keydelay" variable is there to accommodate for this. 
    keydelay = 0 if platform.system() == 'Windows' else 1
    hours, minutes, seconds = seconds_to_time(int(4*(delay+keydelay+0.2)*no_of_tps))

    print(f'This will teleport to {no_of_tps} different locations.')
    print(f'It will take approximately {hours}h {minutes}m {seconds}s.\n')
    time.sleep(1)
    print('*** IMPORTANT ***')
    print('Once you continue, you will have 10 seconds before the script begins typing.') 
    print('Remember to make Minecraft the active window before then! \n')
    
    # Get user confirmation
    answer = input('Do you wish to proceed? [y/n]: ')
    if answer.lower() != 'y':
        print('"n" or invalid answer entered. Aborting.')
        return
    
    print('You have 10 seconds to make Minecraft the active window.')
    time.sleep(7)
    print('Starting in 3')
    time.sleep(1)
    print('Starting in 2')
    time.sleep(1)
    print('Starting in 1')
    time.sleep(1)
    print('Starting teleports...')
    
    start_time = int(time.time())
    execute_commands(x_min, x_no_steps, z_min, z_no_steps, height, step_size, delay)
    end_time = int(time.time())
    
    hours_taken, minutes_taken, seconds_taken = seconds_to_time(end_time - start_time)
    print(f'Teleports complete in {hours_taken}h {minutes_taken}m {seconds_taken}s')


if __name__ == '__main__':
    # Format: (xmin, xmax, zmin, zmax, no of blocks between tps, tp delay in seconds)
    main(-2880, 2880, -2880, 2880, 192, 240, 2)
