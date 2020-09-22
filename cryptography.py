from PIL import Image, ImageFont, ImageDraw  

def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)
    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]
    red_pixels = red_channel.load()
    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size
    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    for x in range(x_size):
        for y in range(y_size):
            red_binary_str = bin(red_pixels[x, y])
            if int(red_binary_str[len(red_binary_str)-1]) == 0:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("my_decoded_image.png")

def write_text(size, text):
  """
  Writes a text in black to a white image and returns it.
  """
  img = Image.new('RGB', size, (255, 255, 255))
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype('/Library/Fonts/Arial.ttf')
  draw.text((10,10), text, (0, 0, 0))
  return img

def encode_image(path_to_png):
  """
  TODO: Add docstring and complete implementation.
  """
  img = write_text((1000, 1000), 'hidden words revealed')
  img.save(path_to_png)

encode_image("encoded.png")


# def round_red_channel(image):
#     '''
#     Args:
#         image (PIl image file): realtive or absolute path to png
    
#     Returns:
#         image with all it's channel rounded down
    
#     Raises:
#         TypeError: arg image is not a PIL image file
#     '''
#     img = Image.open('myencode.png').convert('RGB')
#     width, _ = img.size
#     for i, px in enumerate(img.getdata()):
#         if px[:3] == (255, 255, 255):
#             y = i / width
#             x = i % width
#             img.putpixel((x, y), (255, 0, 0))

#     img.save('myencode-red.png')

if __name__ == '__main__':
    decode_image('./myencode.png')
   