# Модуль выполнил Горошко В.И.
from PIL import Image #Загрузка требуемых библиотек
from re import findall


def stega_decrypt(): #Создание функции
    char = [] #Массив для значений символов
    msg = ''
    keys = [] # Массив для ключей
    img = Image.open(input("path to image: ")) # Создание переменной изображения
    pix = img.load()  #Загрузка данных пикселя изображения
    f = open(input('path to keys: '), 'r') # Текстовый файл откуда берутся ключи
    y = str([line.strip() for line in f]) # Переменная строки файла

    for i in range(len(findall(r'\((\d+)\,', y))): # Цикл для извлечения ключей из файла
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys: # Цикл добавления значений символов в массив
        char.append(pix[tuple(key)][2])
    for elem in char:
        msg += chr(elem)
    return msg 


print("your message: ", stega_decrypt()) # Вывод сообщения

