from PIL import Image

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
    decoded_image.save("decoded_image.png")

def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # raw_image = Image.open(path_to_png).convert("RGB")
    # round_red_channel(raw_image)
    # msg_image = Image.new("RGB",raw_image.size,(0,0,0))

    # msg = ImageDraw.Draw(msg_image)
    # msg.multiline_text((10,10), text_to_write, fill=(1,0,0))
    # msg_image.save('Savedtext.png')

    # encoded_image = ImageChops.add(raw_image,msg_image)
    # encoded_image.save('encoded_image.png')

# def round_red_channel(image):
#     '''
    # Args:
    #     image (PIl image file): realtive or absolute path to png
    
    # Returns:
    #     image with all it's channel rounded down
    
    # Raises:
    #     TypeError: arg image is not a PIL image file
    # '''
    # # pixels = image.load()
    # # x_size, y_size = image.size
    # # for i in range(0,x_size):
    # #     for j in range(0, y_size):
    # #         pixel = pixels[i,j]
    # #         pixels[i,j] = (pixel[0] - pixel[0]%2,pixel[1],pixel[2])

if __name__ == '__main__':
    decode_image('./encoded_sample.png')