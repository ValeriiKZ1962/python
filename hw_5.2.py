# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке

my_list = ['Здесь\n', 'Тут\n', 'Везде\n']
with open("text.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("text.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"Number of lines is {lines}")
