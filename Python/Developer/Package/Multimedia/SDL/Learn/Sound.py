import sdl2
import sdl2.sdlmixer

# Initialize SDL2 Mixer
sdl2.sdlmixer.Mix_OpenAudio(44100, sdl2.sdlmixer.MIX_DEFAULT_FORMAT, 2, 2048)

# Load and play sound
sound = sdl2.sdlmixer.Mix_LoadWAV(b"..\\Media\\sound.wav")
sdl2.sdlmixer.Mix_PlayChannel(-1, sound, 0)

# Keep the program running to hear the sound
input("Press Enter to exit...")
sdl2.sdlmixer.Mix_FreeChunk(sound)
sdl2.sdlmixer.Mix_CloseAudio()
