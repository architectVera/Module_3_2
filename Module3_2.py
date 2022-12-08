# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Product:
    """This class describes a product"""

    def __init__ (self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def calc_product_total(self, quantity):
        return round(float(self.price*quantity), 2)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __repr__(self):
        return f'Product (name = {self.name}, price = {self.price})'

    def __str__(self):
        return f'Name of product  is {self.name}, its price is {self.price})'

    def __float__(self):
        return  float(self.price)


class ShoppingCart():
    """This class describes a ShoppingCart

    Attributes
    __________
    cart : list
    quantity_cart: list

    Methods
    __________
    add_to_cart(self, product: Product, quantity: int)
        Adds a product to the cart and adds the quantity to the quantity_cart

    calc_total(self)
        Calculates the total price of all products added to the cart
    """
    def __init__(self):
        self.cart = []
        self.quantity_cart = []

    def __repr__(self):
        return f'ShoppingCart (cart = {self.cart}, quantity_cart = {self.quantity_cart})'

    def __float__(self):
        return  self.calc_total()

    def add_to_cart(self, product: Product, quantity: int):
        """Adds  a product to the cart and adds the quantity to the quantity_cart."""

        if not isinstance(product, Product):
            raise RuntimeError("You can only add instances of the class Product")

        if product in self.cart:
            index_product = self.cart.index(product)
            self.quantity_cart[index_product] += quantity
        else:
            self.cart.append(product)
            self.quantity_cart.append(quantity)


    def calc_total(self):
        """Calculates the total price of all products added to the cart."""

        total = 0
        for p in range(len(self.cart)):
            total += self.cart[p].calc_product_total(self.quantity_cart[p])
        return total

    def __add__(self, other):
        """Combines two carts into one"""

        joined_cart = ShoppingCart()
        joined_cart.cart += self.cart
        joined_cart.quantity_cart += self.quantity_cart
        if not isinstance(other, (Product, ShoppingCart)):
            raise RuntimeError("You can only add to instances of the class ShoppingCart")
        for product, quantity in zip(other.cart, other.quantity_cart):
            joined_cart.add_to_cart(product, quantity)
            return joined_cart


apple = Product("apple", 30)
orange = Product("orange",50)

cart_1 = ShoppingCart()
cart_2 = ShoppingCart()

cart_2.add_to_cart(orange, 2)
#
cart_1.add_to_cart(orange, 4)
cart_1.add_to_cart(orange, 4)
cart_1.add_to_cart(apple, 2)

our_cart = cart_1 + cart_2
print(our_cart.quantity_cart)
for p in our_cart.cart:
    print(p.name)
print(our_cart.calc_total())
print(apple.__repr__())
print(apple.__str__())
print(our_cart.__float__())
