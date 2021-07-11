# Lightbike
The light bicycle game: have fun trying to defeat your opponent by forcing 
them to run into the trails created by your bike. Alternatively, force them 
to crash into the wall! First one to crash loses!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and arcade 2.5.7 or newer installed 
and running on your machine. You can install arcade by opening a terminal 
and running the following command.
```
python3 -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 lightbike
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the lightbike folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- docs                (project documentation)
+-- lightbike           (src code files - lightbike)
  +-- assets            (program asset files)
    +-- __init__.py
    +-- blue_player.png
    +-- blue_power.png
    +-- blue_wall.png
    +-- floor_mosaic.png
    +-- mi_explosion_03_hpx.wav
    +-- orange_player.png
    +-- orange_power.png
    +-- orange_wall.png
    +-- Sci-Fi-Dramatic-Theme.wav
    +-- wall_1.png
    +-- wall_2.png
    +-- wall_3.png
    +-- wall_4.png
    +-- wall_5.png
    +-- wall_6.png
  +-- data              (program data files)
    +-- __init__.py
    +-- action.py
    +-- actor.py
    +-- ai.py
    +-- constants.py
    +-- control_actors_action.py
    +-- draw_actors_action.py
    +-- game.py
    +-- handle_collisions_action.py
    +-- lightbike.py
    +-- map.py
    +-- move_actors_action.py
    +-- output_service.py
    +-- player.py
    +-- trail.py
  +-- tests             (program test files)
    +-- test_actor.py
    +-- test_ai.py
    +-- test_lightbike.py
    +-- test_map.py
    +-- test_player.py
    +-- test_point.py
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- LICENSE             (license file)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* arcade 2.5.7

## Authors
---
* Rich Abbott: rich.abbott3@gmail.com
* Ethan Charles: ethan.charles02@gmail.com
* Avery Crowson: crowson.avery@gmail.com
* Hunter Dunlap: hwd14@rocketmail.com
* Miguel Marin: mar19013@byui.edu
