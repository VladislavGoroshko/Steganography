# Модуль выполнил Горошко В.И.
from PIL import Image, ImageDraw #Загрузка требуемых библиотек
from random import randint


def stega_encrypt(): #Создание функции
    keys = []  # Массив для ключей
    img = Image.open(input("path to image: "))  # Создание переменной изображения
    drw = ImageDraw.Draw(img)  # #Создание пишущего пера
    wdt = img.size[0]  #Переменная ширины изображения
    hgt = img.size[1]  #Переменная высоты изображения
    pix = img.load()  #Загрузка данных пикселя изображения
    f = open('keys.txt', 'w')  # Текстовый файл куда будут записываться ключи

    for elem in ([ord(elem) for elem in input("secret message: ")]): #Ввод сообщения и цикл по символам
        key = (randint(1, wdt-1), randint(1, hgt-1)) #генерирование ключа
        r, g = pix[key][0:2] #Запоминание исходных цветовых каналов красный и зеленый
        drw.point(key, (r, g, elem)) #Рисование измененного пикселя
        f.write(str(key) + '\n') #Запись ключа в файл
    print('keys were written to the keys.txt file')
    img.save("2.png", "PNG")
    f.close()

stega_encrypt()

