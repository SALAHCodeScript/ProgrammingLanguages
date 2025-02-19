import sdl2
import sdl2.ext

# Initialize SDL2
sdl2.ext.init()

# Create a window and renderer
window = sdl2.SDL_CreateWindow(b"PySDL2 Renderer", sdl2.SDL_WINDOWPOS_CENTERED,
                               sdl2.SDL_WINDOWPOS_CENTERED, 640, 480, sdl2.SDL_WINDOW_SHOWN)
renderer = sdl2.SDL_CreateRenderer(window, -1, sdl2.SDL_RENDERER_ACCELERATED)

# Event loop
running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False

    # Set draw color (R, G, B, A)
    sdl2.SDL_SetRenderDrawColor(renderer, 5, 5, 8, 255)  # Blue background
    sdl2.SDL_RenderClear(renderer)  # Clear screen with blue

    # Set color and draw a rectangle
    sdl2.SDL_SetRenderDrawColor(renderer, 0, 200, 150, 255)  # Red color
    rect = sdl2.SDL_Rect(200, 150, 240, 180)
    sdl2.SDL_RenderFillRect(renderer, rect)  # Fill rectangle

    sdl2.SDL_RenderPresent(renderer)  # Update screen

# Cleanup
sdl2.SDL_DestroyRenderer(renderer)
sdl2.SDL_DestroyWindow(window)
sdl2.ext.quit()
