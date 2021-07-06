# Minecraft Pre-generator
A simple Python script to generate a sequence of `/tp` commands intended to pre-generate a Minecraft world.

This was inspired by [Xisumavoid's video on pre-generating the Hermitcraft season 7 world](https://www.youtube.com/watch?v=eA35S2GW-jI).

## What does it do?
The script uses [the `keyboard` Python module](https://github.com/boppreh/keyboard) to generate and type out `/tp` commands, which teleport the player in a grid pattern spaced 240 blocks apart. For each location teleported to, the player is rotated in all four compass directions (North, East, South, then West) and waits a given amount of time between teleports, to give Minecraft the best opportunity to generate chunks around the player's location. 

## Running the script
To run this script for yourself, make sure you have Python 3 installed. You will also need the `keyboard` module, which you can get with:

    pip3 install keyboard

By default, the script is set to teleport the player over an area of 5760x5760 centred on the origin. Teleports are spaced 240 blocks apart, and it waits for 2 seconds between teleports. If you just want to run the script with these default settings, then you only need to download `script.py` and run it:

    python3 script.py

### Custom values

If you want to enter custom values for the coordinates, teleport spacing, and teleport delay, you should also download `interface.py`. Make sure it is in the same directory as `script.py`, then run `interface.py`:

    python3 interface.py

### IMPORTANT NOTE

Once you answer `y` in the script, you will have 10 seconds to make Minecraft the active window before the script starts typing the commands!