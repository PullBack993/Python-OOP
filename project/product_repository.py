from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        find_product = [p for p in self.products if product_name == p.name][0]
        return find_product

    def remove(self, product_name):
        remove_product = [p for p in self.products if product_name == p.name][0]
        del remove_product
        


    def __repr__(self):
        result = ""
        for p in range(len(self.products)):
            if p+1 < len(self.products):
                result += f"{self.products[p].name}: {self.products[p].quantity}\n"
            else:
                result += f"{self.products[p].name}: {self.products[p].quantity}"

        return result
