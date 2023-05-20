from PIL import Image, ImageDraw, ImageFont


card = Image.open("bbdk.jpg.")


width, height = card.size


draw = ImageDraw.Draw(card)


font = ImageFont.truetype("arial.ttf", 36)


name = input("Введите имя: ")


text = name + ", поздравляю!"
text_width, text_height = draw.textsize(text, font)
x = (width - text_width) / 2
y = height * 0.1
draw.text((x, y), text, font=font, fill=(255, 0, 0, 255))


card.save("new_birthday_card.png", "PNG")