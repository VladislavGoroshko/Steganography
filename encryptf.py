from PIL import Image, ImageDraw # Загрузка требуемых библиотек
from random import randint

def stega_encrypt(): # Создание функции
    keys = []  # Массив для ключей
    img = Image.open(input("path to image: ")) # Создание переменной изображения
    drw = ImageDraw.Draw(img) # Создание пишущего пера
    wdt = img.size[0] # Переменная ширины изображения
    hgt = img.size[1] # Переменная высоты изображения
    pix = img.load() # Загрузка данных пикселя изображения
    f = open('keys.txt', 'w')  # Текстовый файл куда будут записываться ключи
    msg = input("secret message: ") # Переменная строки сообщения
    if len(msg) > int((wdt * 0.7)) * int((hgt * 0.7)): # Проверка допустимости объёма сообщения
        print('Error! The message size exceeds the allowed size.') # Ошибка объёма изображения
    else:
        for elem in ([ord(elem) for elem in msg]): # Ввод сообщения и цикл по символам
            bi = bin(elem) # Перевод в двоичную систему счисления
            bi = bi[2:] # Перевод в двоичную систему счисления
            oc = '0' * (8 - len(bi)) + bi # Преобразование в 8-битный вид
            for k in oc: # Цикл встраивания
                key = (randint(1, wdt-1), randint(1, hgt-1))  # генерирование ключа
                r, g = pix[key][0:2] # Запоминание исходных цветовых каналов красный и зеленый
                b = pix[key][2] # Получение синего цветового канала
                b = bin(b) # Перевод в двоичную систему счисления
                b = b[2:(len(b) - 1)] + k # Изменение последнего бита
                b = int(b, 2) # Перевод в десятичную систему счисления
                drw.point((key), (r, g, b)) # Рисование измененного пикселя
                f.write(str(key) + '\n')  # Запись ключа в файл
        print('keys were written to the keys.txt file') # Сообщение о записи ключей
        img.save("2.png", "PNG") # Сохранение нового изображения
        f.close() # Закрытие файла

stega_encrypt()