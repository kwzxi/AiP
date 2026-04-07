from PIL import Image, ImageDraw, ImageFont

#Создаем словарь открыток
cards = {
    "Новый год": "new_year.jpg",
    "8 марта": "march8.jpg",
    "День рождения": "birthday.jpg",
    "23 февраля": "feb23.jpg"
}
holiday = input("К какому празднику нужна открытка? ")
name = input("Введите имя для поздравления: ")

# Проверяем есть ли такой праздник в словаре
if holiday in cards:

    img = Image.open(cards[holiday])
    # Обрезаем часть изображения
    # координаты: (лево, верх, право, низ)

    width, height = img.size
    cropped = img.crop((0, 0, width, height - 50))  # обрезаем нижнюю часть

    # Сохраняем обрезанное изображение
    cropped.save("cropped_postcard.jpg")

    #  Добавляем текст на открытку

    draw = ImageDraw.Draw(cropped)

    # Подключаем шрифт 
    font = ImageFont.truetype("arial.ttf", 50)

    # Текст поздравления
    text = f"{name}, поздравляю!"

    # Определяем координаты текста
    text_width, text_height = draw.textsize(text, font=font)

    # Центрируем текст сверху
    x = (width - text_width) // 2
    y = 20


    # Делаем жирный текст
    # (рисуем несколько раз со смещением)

    draw.text((x, y), text, font=font, fill="red")
    draw.text((x+1, y), text, font=font, fill="red")
    draw.text((x, y+1), text, font=font, fill="red")
    draw.text((x+1, y+1), text, font=font, fill="red")

    # cохраняем готовую открытку в PNG
    cropped.save("final_postcard.png")

    # показываем результат
    cropped.show()
else:
    print("Открытка для такого праздника не найдена")