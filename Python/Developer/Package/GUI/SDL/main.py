import sdl2
import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("SDL with PySDL2", size=(640, 480))
window.show()

running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False

sdl2.ext.quit()
