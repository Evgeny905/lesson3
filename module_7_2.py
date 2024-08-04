def custom_write(file_name, strings):
    strings_positions = {}
    a = 0
    for str in strings:
        file = open(file_name, 'a', encoding = 'utf-8')
        Kursor = file.tell()
        file.write(f'{str}\n')
        a = a + 1
        strings_positions[a, Kursor] = (str)
        file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)