from PIL import Image

image = Image.open("bitcoin.png")
image = image.resize((101, 101), Image.ANTIALIAS)
image.save(fp="bitcoin.png")