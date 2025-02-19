import sdl2
import sdl2.ext
import sdl2.sdlttf

# Initialize SDL2 and TTF
sdl2.ext.init()
sdl2.sdlttf.TTF_Init()

# Create a window and renderer
window = sdl2.SDL_CreateWindow(b"Text Rendering", sdl2.SDL_WINDOWPOS_CENTERED,
                               sdl2.SDL_WINDOWPOS_CENTERED, 640, 480, sdl2.SDL_WINDOW_SHOWN)
renderer = sdl2.SDL_CreateRenderer(window, -1, sdl2.SDL_RENDERER_ACCELERATED)

# Load a font (change path to an existing .ttf font)
font = sdl2.sdlttf.TTF_OpenFont(b"..\\Assest\\font.ttf", 32)

# Set text color (white)
color = sdl2.SDL_Color(255, 255, 255, 255)

# Render text to a surface
text_surface = sdl2.sdlttf.TTF_RenderText_Solid(font, b"Hello, PySDL2!", color)

# Convert the surface to a texture
text_texture = sdl2.SDL_CreateTextureFromSurface(renderer, text_surface)

# Get texture width and height
w, h = text_surface.contents.w, text_surface.contents.h
dst_rect = sdl2.SDL_Rect(200, 200, w, h)

# Free the surface
sdl2.SDL_FreeSurface(text_surface)

# Event loop
running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False

    # Clear and draw text
    sdl2.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)  # Black background
    sdl2.SDL_RenderClear(renderer)
    sdl2.SDL_RenderCopy(renderer, text_texture, None, dst_rect)
    sdl2.SDL_RenderPresent(renderer)

# Cleanup
sdl2.SDL_DestroyTexture(text_texture)
sdl2.sdlttf.TTF_CloseFont(font)
sdl2.SDL_DestroyRenderer(renderer)
sdl2.SDL_DestroyWindow(window)
sdl2.sdlttf.TTF_Quit()
sdl2.ext.quit()
