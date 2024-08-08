class WordsFinder:
    def __init__(self, *file):
        self.file = file
        self.file_names = []
        for i in self.file:
            self.file_names.append(i)
            file_name = i
            file = open(file_name, 'w')
            file.write("It's a text for task Найти везде\nИспользуйте его для самопроверки.\nУспехов в решении задачи!\ntext text text")
            file.close()
    def get_all_words(self):
        all_words = {}
        all_line = []
        for j in self.file_names:
            with open(j) as file:
                for line in file:
                    line = line.lower()
                    line = line.replace(',', '')
                    line = line.replace('.', '')
                    line = line.replace('=', '')
                    line = line.replace('!', '')
                    line = line.replace('?', '')
                    line = line.replace(';', '')
                    line = line.replace(':', '')
                    line = line.replace('-', '')
                    line = line.split()
                    all_line.extend(line)
                    all_words[j] = (all_line)
        return all_words
    def find(self, word):
        self.word = word.lower()
        Position_words = {}
        all_words = WordsFinder.get_all_words(self)
        a = 1
        for key, value in all_words.items():
            for Slovo in value:
                if Slovo == self.word:
                    Position_words[key] = (a)
                    break
                else:
                    a = a + 1
                    continue
        return Position_words
    def count(self, word):
        self.word = word.lower()
        Kol_vo_words = {}
        all_words = WordsFinder.get_all_words(self)
        a = 0
        for key, value in all_words.items():
            for Slovo in value:
                if Slovo == self.word:
                    a = a + 1
                elif Slovo != self.word:
                    continue
                Kol_vo_words[key] = (a)
        return Kol_vo_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего