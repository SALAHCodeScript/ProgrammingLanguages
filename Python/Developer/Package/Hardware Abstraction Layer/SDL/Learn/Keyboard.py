import sdl2
import sdl2.ext

sdl2.ext.init()
window = sdl2.ext.Window("Event Handling", size=(640, 480))
window.show()

running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
        elif event.type == sdl2.SDL_KEYDOWN:  # Keyboard press
            print(f"Key Pressed: {event.key.keysym.sym}")
        elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:  # Mouse click
            print(f"Mouse Click at ({event.button.x}, {event.button.y})")

sdl2.ext.quit()
