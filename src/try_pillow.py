from PIL import Image, ImageDraw

image = Image.new("RGB", (100, 100), "white")

draw = ImageDraw.Draw(image)

draw.line((10, 10, 90, 90), fill="red", width=3)

image.save("example.png")
image.show()
