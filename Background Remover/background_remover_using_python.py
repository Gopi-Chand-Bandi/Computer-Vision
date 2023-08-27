from rembg import remove
from PIL import Image

inputpath="C:/Users/91817/Downloads/download.jpeg"

input=Image.open(inputpath)

output = remove(input)

output.save("C:/Users/91817/Downloads/TomCruise2.png")
output_path = "C:/Users/91817/Downloads/TomCruise2.png"
output_image = Image.open(output_path)
output_image.show()