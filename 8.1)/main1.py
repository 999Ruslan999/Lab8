from PIL import Image


image = Image.open("x55271.jpg")


cropped_image = image.crop((100, 100, 400, 400))


cropped_image.save("new_photo.jpg")