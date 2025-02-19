import png

# Create a 5x5 grayscale image with pixel values ranging from 0 (black) to 255 (white)
image = [
    [0, 50, 100, 150, 200],
    [50, 100, 150, 200, 250],
    [100, 150, 200, 250, 255],
    [150, 200, 250, 255, 255],
    [200, 250, 255, 255, 255]
]

# Save the image as a PNG file
with open("../Images/output.png", "wb") as f:
    writer = png.Writer(width=5, height=5, greyscale=True, bitdepth=8)
    writer.write(f, image)

# Read an existing PNG file
reader = png.Reader(filename="../Images/output.png")
width, height, pixels, metadata = reader.read()

# Convert pixels to a list
pixel_list = list(pixels)

# Display details of PNG file
print(f"Width: {width}, Height: {height}")
print("First row of pixels:", pixel_list[0])
