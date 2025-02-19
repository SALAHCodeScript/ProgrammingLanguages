import sdl2
import sdl2.ext

# Initialize SDL2
sdl2.ext.init()

# Create a hardware-accelerated window and renderer
window = sdl2.SDL_CreateWindow(b"Hardware Acceleration", sdl2.SDL_WINDOWPOS_CENTERED,
                               sdl2.SDL_WINDOWPOS_CENTERED, 640, 480, sdl2.SDL_WINDOW_SHOWN)
renderer = sdl2.SDL_CreateRenderer(window, -1, sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_PRESENTVSYNC)

# Load an image as a texture (use an existing image file)
image = sdl2.ext.load_image("D:\\Data\\SALAH\\home\\salah\\Pictures\\Favor\\Yoru.jpg")
texture = sdl2.SDL_CreateTextureFromSurface(renderer, image)

# Free the surface after creating the texture
sdl2.SDL_FreeSurface(image)

running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False

    # Clear screen
    sdl2.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)
    sdl2.SDL_RenderClear(renderer)

    # Render texture
    sdl2.SDL_RenderCopy(renderer, texture, None, None)

    # Present the rendered frame
    sdl2.SDL_RenderPresent(renderer)

# Cleanup
sdl2.SDL_DestroyTexture(texture)
sdl2.SDL_DestroyRenderer(renderer)
sdl2.SDL_DestroyWindow(window)
sdl2.ext.quit()
