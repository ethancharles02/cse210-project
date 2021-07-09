# from arcade import Sound
# SOUND_BACKGROUND = Sound("test.mp3")

# SOUND_BACKGROUND.play(0.2, loop=True)


import pyglet
source = pyglet.media.load('test.mp3', streaming=False)
source.play()
pyglet.app.run()
# cancel_input = input()