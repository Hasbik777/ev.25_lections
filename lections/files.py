# Работа с файлами
# каретка - указатель - курсор

# open(<путь до файла>)

# file = open('/home/sanjar/Desktop/evening 25/files/lections/files.py') # абсолютный путь
# file = open('files.py') # оптносительный путь(относительно к той директории в которой вы работаете)

# Режимы работы с файлома
# 1. чтение -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавоения -> a/a+ (append)
# b x t

# file = open('test.txt', 'r')
# print(file.read())
# file.close()


# file = open('test.txt', 'r')
# data = file.read()
# data = data.split('/n')
# print(data)
# print(len(data))
# file.close()

# контекстный менеджер

# with open('test.txt') as file:
#     print(file.tell())
#     data = file.read()
#     index = data.index('My')
#     print(file.tell())
#     file.seek(index)
#     print(file.read())
#     print(file.tell())
    
# file.tell() -> возвращает индекс где находиться указатель(курсор/каретка)
# file.seek(index) -> перемещает каретку на индекс который вы передали

# with open('test.txt', 'r') as file:
#     print(file.readlines())
#     file.seek(0)
#     print(file.readline())
#     print(file.readline())



# with open('test.txt', 'a+') as f:
#     f.write('\nHe is bastard of Ned Starka!')
#     f.write('\nThis is lesson about files!')
#     f.seek(0)
#     print(f.read())


# with open('test.txt', 'w') as f:
#     f.write('Hello, file was opened with open!')

# --------------------------------------------------------
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re        
# def get_imei_codes(image):
#     string = pytesseract.image_to_string(image)
#         # print(string)
#     list_of_imei = re.findall(r'IME.\d.\s\d+', string)
#     print(list_of_imei)
#     with open('imei_codes.txt', 'w') as file:
#         for x in list_of_imei:
#             file.write(f'{x}\n')    
# ls = 'imei.jpg'
# get_imei_codes(ls)


