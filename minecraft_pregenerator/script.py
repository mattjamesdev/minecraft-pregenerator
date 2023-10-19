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

    Parameters:
    seconds (int)
        A time duration in seconds.

    Returns:
    (tuple[int, int, int])
        The number of hours, minutes, and seconds.
    """
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)
    return hours, minutes, seconds


# Generate the command to write.
# location is a 3-tuple (x, y, z) of the desired coordinates
def tp_command(location, yaw=-180.0, pitch=20.0):
    return f'/tp @p {location[0]} {location[1]} {location[2]} {yaw} {pitch}'


# The main bulk of the script.
def command_executer(xmin, x_steps, zmin, z_steps, y_height, step_size, delay):
    for z_step in range(z_steps):
        for x_step in range(x_steps):
            coords = (xmin + step_size*x_step, y_height, zmin + step_size*z_step)
            for n in range(4):
                yaw_angle = -180.0 + n*90
                kb.send('t')
                time.sleep(0.05)
                kb.write(tp_command(coords, yaw_angle))
                time.sleep(0.05)
                kb.send('enter')
                time.sleep(delay)


def main(xmin, xmax, zmin, zmax, height, step_size, delay):
    x_no_steps = int((xmax - xmin)/step_size) + 1
    z_no_steps = int((zmax - zmin)/step_size) + 1
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
    command_executer(xmin, x_no_steps, zmin, z_no_steps, height, step_size, delay)
    end_time = int(time.time())
    
    hours_taken, minutes_taken, seconds_taken = seconds_to_time(end_time - start_time)
    print(f'Teleports complete in {hours_taken}h {minutes_taken}m {seconds_taken}s')


if __name__ == '__main__':
    # Format: (xmin, xmax, zmin, zmax, no of blocks between tps, tp delay in seconds)
    main(-2880, 2880, -2880, 2880, 192, 240, 2)
