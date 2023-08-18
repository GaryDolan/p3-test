# from PIL import Image

# # Load the image
# image_path = "pikachu.png"
# image = Image.open(image_path)

# # Define a string of ASCII characters to use for the art
# ascii_chars = ". "

# # Calculate the width and height of the image
# width, height = image.size
# aspect_ratio = height / width
# new_width = 40
# new_height = int(aspect_ratio * new_width * 0.55)

# # Resize the image
# resized_image = image.resize((new_width, new_height))

# # Convert the image to grayscale
# grayscale_image = resized_image.convert("L")

# # Generate ASCII art
# ascii_art = ""
# for pixel_value in grayscale_image.getdata():
#     ascii_index = pixel_value * len(ascii_chars) // 256
#     ascii_art += ascii_chars[ascii_index]

# # Print the ASCII art
# print(ascii_art)

# with open("ascii_image.txt", "w") as f:
#     f.write(ascii_art)
