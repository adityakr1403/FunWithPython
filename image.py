from PIL import Image

def convert_image_to_ascii(image_file):
    # Open the image file
    with Image.open(image_file) as img:
        # Convert the image to grayscale
        img = img.convert('L')
        # Resize the image
        img = img.resize((100, 100))
        # Define the ASCII characters to use
        ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
        # Get the pixel values of the image
        pixels = img.load()
        # Create an empty list to store the ASCII characters
        ascii_image = []
        # Iterate over the rows and columns of the image
        for row in range(img.height):
            ascii_row = ""
            for col in range(img.width):
                # Get the pixel value at the current position
                pixel_value = pixels[col, row]
                # Determine the ASCII character to use for the pixel value
                ascii_char = ASCII_CHARS[pixel_value // 25]
                ascii_row += ascii_char
            ascii_image.append(ascii_row)
        return "\n".join(ascii_image)
print(convert_image_to_ascii("adityakr1403.png"))
