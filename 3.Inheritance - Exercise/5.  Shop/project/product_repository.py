from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        find_product = [p for p in self.products if product_name == p.family_name][0]
        return find_product

    def remove(self, product_name):
        for el in self.products:
            if el.family_name == product_name:
                self.products.remove(el)



    def __repr__(self):
        result = ""
        for p in range(len(self.products)):
            if p+1 < len(self.products):
                result += f"{self.products[p].family_name}: {self.products[p].quantity}\n"
            else:
                result += f"{self.products[p].family_name}: {self.products[p].quantity}"

        return result
