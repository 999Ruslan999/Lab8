from PIL import Image


holidays = {
    "Новый год": "ng.jpg",
    "День рождения": "gr.jpg",
    "8 Марта": "8m.jpg"
}


holiday = input("Введите название праздника: ")


filename = holidays.get(holiday)

if filename:

    image = Image.open(filename)
    image.show()
else:
    print("Открытка для данного праздника не найдена")