
# 9.12. Построить равнобедренный треугольник с основанием a и высотой h.

from PIL import Image, ImageDraw

a_base = int(input("Введите длину основания треугольника: "))
hight = int(input("Введите длину высоты треугольника: "))
x = int(input("Введите X: "))
y = int(input("Введите Y: "))
x_a = x + a_base
y_h = y + hight
half_x_a = x + (a_base / 2)
y_minus_h = y - hight

img = Image.new("RGB", (1024, 1024), (194, 185, 255))
draw = ImageDraw.Draw(img)
draw.polygon((x, y, half_x_a, y_minus_h, x_a, y), fill=(255, 193, 255))
draw.line((x, y, x_a, y), fill=(255, 88, 213))
draw.line((half_x_a, y, half_x_a, y_minus_h), fill=(142, 202, 255))
img.save('sample.png')
img.show()
