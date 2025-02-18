# Task_3
# Class of goods in the store


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0  # Ініціалізуємо знижку 0%


class Product(Item):
    def __init__(self, product_type, name, price):
        super().__init__(name, price)
        self.product_type = product_type


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add_product(self, product, amount):
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price_premium': product.price * 1.30  # Додаємо 30% націнки
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product_info in self.products.values():
            product = product_info['product']
            identifier_matches = (
                (identifier_type == 'name' and product.name == identifier) or
                (identifier_type == 'type' and
                 product.product_type == identifier))

            if identifier_matches:
                product.discount = percent

    def sell_product(self, product_name, amount):
        if product_name not in self.products or \
           self.products[product_name]['amount'] < amount:
            raise ValueError("Not enough product available")

        product_info = self.products[product_name]
        product_info['amount'] -= amount
        product_price = (
            product_info['price_premium'] *
            (1 - (product_info['product'].discount / 100))
        )
        self.income += product_price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [{
            'name': product_name,
            'amount': product_info['amount'],
            'price': product_info['product'].price,
            'price_premium': product_info['price_premium'],
            'discount': product_info['product'].discount
        } for product_name, product_info in self.products.items()]

    def get_product_info(self, product_name):
        if product_name in self.products:
            product_info = self.products[product_name]
            return product_name, product_info['amount']
        else:
            raise ValueError("Product not found")


if __name__ == "__main__":
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)

    s = ProductStore()

    s.add_product(p, 10)
    s.add_product(p2, 300)
    s.sell_product('Ramen', 10)

    assert s.get_product_info('Ramen') == ('Ramen', 290)
    print("Tests passed!")
