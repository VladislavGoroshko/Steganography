from PIL import Image #Загрузка требуемых библиотек
from re import findall

def stega_decrypt(): # Создание функции
    msg = '' # Переменная строки сообщения
    char = '' # Переменная строки символа
    keys = [] # Массив для ключей
    img = Image.open(input("path to image: ")) # Создание переменной изображения
    pix = img.load()  # Загрузка данных пикселя изображения
    f = open(input('path to keys: '), 'r') # Текстовый файл откуда берутся ключи
    y = str([line.strip() for line in f]) # Переменная строки файла
    for i in range(len(findall(r'\((\d+)\,', y))): # Цикл для извлечения ключей из файла
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys: # Цикл добавления значений символов в массив
        b = int(pix[tuple(key)][2])  # Получение синего цветового канала
        b = bin(b)  # Перевод в двоичную систему счисления
        b = b[len(b) - 1]  # Получение последнего бита
        char += str(b)  # Запись последнего бита
        if len(char)==8: # Цикл записи символа в строку сообщения
            char = int(char, 2) # Перевод значения символа в десятичную систему счисления
            msg += chr(char) # Запись символа в строку сообщения
            char = '' # Очистка строки символа
    return msg # Вывод полученного сообщения

print("your message: ", stega_decrypt())






