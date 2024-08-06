file_name = 'products.txt'
file = open(file_name, 'a')
file.write('')
file.close()
class Produkt:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        self.file = open(self.__file_name, 'r')
        return self.file.read()
        self.file.close()
    def add(self, *products):
        self.products = products
        for product in self.products:
            Poisk = Shop.get_products(self).find(product.name)
            if Poisk != -1:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                self.file.close()

s1 = Shop()
p1 = Produkt('Potato', 50.5, 'Vegetables')
p2 = Produkt('Spaghetti', 3.4, 'Groceries')
p3 = Produkt('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
