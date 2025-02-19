import sys
import sdl2
import sdl2.ext

def main():
    # Initialize SDL
    sdl2.ext.init()

    # Create a Window
    window = sdl2.ext.Window("SDL Multimedia Example", size=(800, 600))
    window.show()

    # Create a Renderer
    renderer = sdl2.ext.Renderer(window)

    # Load an Image (Ensure 'image.png' exists in the directory)
    factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
    image = factory.from_image("D:\\Data\\SALAH\\home\\salah\\Pictures\\Favor\\Yoru.jpg")

    running = True
    while running:
        renderer.clear()  # Clear the screen
        renderer.copy(image, dstrect=(100, 100, 600, 400))  # Draw the image
        renderer.present()  # Update the screen

        # Event Loop
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False

    sdl2.ext.quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
