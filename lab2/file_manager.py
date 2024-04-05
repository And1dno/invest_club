import os
import shutil

working_directory = '' #чтобы программа работала нужно ввести в терминале pwd и полученную строку вставить в значение этой переменной

#Andrey

def create_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    os.mkdir(folder_path)
    print(f"Папка {folder_name} была создана по адресу {folder_path}")


def delete_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    os.rmdir(folder_path)
    print(f"Папка {folder_name} была удалена из {working_directory}")


def change_folder(folder_name):
    global working_directory
    if folder_name == '..':
        working_directory = os.path.dirname(working_directory)
        print("Поднялись на директорию вверх")
    else:
        new_path = os.path.join(working_directory, folder_name)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            working_directory = new_path
            print(f"Переключились на путь {working_directory}")



        else:
            print(f"Папки не существует")


#Davud
def create_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'w'):
        pass
    print(f"Файл {file_name} успешно создан")


def write_to_file(file_name, text):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Текст успешно записан в файл {file_name}")


def view_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Содержимое файла:\n", content)


def delete_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    os.remove(file_path)
    print(f"Файл {file_name} удален")


#Ildar

def copy_file(source_file, destination_folder):
    source_path = os.path.join(working_directory, source_file)
    destination_path = os.path.join(working_directory, destination_folder, source_file)
    shutil.copyfile(source_path, destination_path)
    print(f"файл {source_file} скопирован в {destination_path}")


def move_file(source_file, destination_folder):
    source_path = os.path.join(working_directory, source_file)
    destination_path = os.path.join(working_directory, destination_folder, source_file)
    shutil.move(source_path, destination_path)
    print(f"Файл {source_file} перемещен в {destination_path}")


def rename_file(old_name, new_name):
    old_path = os.path.join(working_directory, old_name)
    new_path = os.path.join(working_directory, new_name)
    os.rename(old_path, new_path)
    print(f"Файл {old_name} переименован в {new_name}")


def fileslist():
    files = os.listdir(working_directory)
    for file in files:
        print(file)

#Отсюда я, пните когда запушите все куски кода чтобы я мог собрать основную часть работы
'''
mode = 0
while mode != -1:
    try:
        print('Выберите 1 чтобы создать папку')
        print('Выберите 2 чтобы удалить папку')
        print('Выберите 3 чтобы сменить рабочую папку')
        print('Выберите 4 чтобы создать файл')
        print('Выберите 5 чтобы записать текст в файл')
        print('Выберите 6 чтобы посмотреть содержимое файла')
        print('Выберите 7 чтобы удалить файл')
        print('Выберите 8 чтобы скопировать файл')
        print('Выберите 9 чтобы переместить файл')
        print('Выберите 10 чтобы переименовать файл')
        print('Выберите 11 чтобы посмотреть список файлов в текущей директории')
        print('Выберите -1 чтобы выйти из программы')
        mode = int(input())
        if mode == 1:
            folder = str(input('Введите имя папки которую хотите создать: '))
            create_folder(folder)
        elif mode == 2:
            folder = str(input('Введите имя папки которую хотите удалить: '))
            delete_folder(folder)
        elif mode == 3:
            print(
                "Введите '..' если хотите перейти на директорию выше или введите название папки в которую хотите переключиться: ")
            folder = str(input())
            change_folder(folder)
        elif mode == 4:
            file = str(input('Введите имя файла который хотите создать: '))
            create_file(file)
        elif mode == 5:
            file = str(input('Введите имя файла который хотите создать: '))
            text = str(input('Введите текст который хотите записать в файл: '))
            write_to_file(file, text)
        elif mode == 6:
            file = str(input('Введите имя файла который вы хотите просмотреть: '))
            view_file(file)
        elif mode == 7:
            file = str(input('Введите имя файла который хотите удалить: '))
            delete_file(file)
        elif mode == 8:
            file = str(input('Введите имя файла который хотите скопировать: '))
            dest_dir = str(input('Введите имя папки в которую вы хотите скопировать файл'))
            copy_file(file, dest_dir)
        elif mode == 9:
            file = str(input('Введите имя файла который хотите переместить: '))
            dest_dir = str(input('Введите имя папки в которую вы хотите переместить файл: '))
            move_file(file, dest_dir)
        elif mode == 10:
            file = str(input('Введите имя файла который хотите переименовать: '))
            new_name = str(input('Введите новое имя файла'))
            rename_file(file, new_name)
        elif mode == 11:
            fileslist()
        elif mode == -1:
            print("До новых встреч!")
        else:
            print("Неизвестная команда")
    except:
        print('неправильный формат ввода')'''
