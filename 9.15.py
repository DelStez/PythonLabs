# Построить квадрат, вписанный в окружность радиуса R.
import math
from PIL import Image, ImageDraw, ImageFont

center_x = int(input("Введите координату 'X' центра окружности: "))
center_y = int(input("Ваедите координату 'Y' центра окружности: "))
R = int(input("Введите длину радиуса R: "))
SQUARE_ROOT_OF_TWO = math.sqrt(2)
d = 2*R
point_on_ellipse = center_x + R
coord_for_text_R = center_x + (R / 2)
y = center_y - R
x1 = center_x - R
y2 = y + d
y3 = center_y - (R/SQUARE_ROOT_OF_TWO)
x3 = center_x - (R/SQUARE_ROOT_OF_TWO)
x4 = center_x + (R/SQUARE_ROOT_OF_TWO)
y4 = center_y + (R/SQUARE_ROOT_OF_TWO)
CONST_IMAGE = Image.new("RGB", (1024, 1024), (255, 255, 255))
draw = ImageDraw.Draw(CONST_IMAGE )
font = ImageFont.truetype("DejaVuSerif.ttf", 16)
draw.ellipse((x1, y, point_on_ellipse, y2), fill=(163, 126, 171))
draw.rectangle((x3, y3, x4, y4), fill=(236, 183, 247))
draw.line((center_x, center_y, point_on_ellipse, center_y), fill="black")
draw.text((x1 - 50, y), "Круг", fill="black", font=font)
draw.text((x4 + 25, y4), 'Квадрат', fill="black", font=font)
CONST_IMAGE.save('sample.png')
CONST_IMAGE.show()