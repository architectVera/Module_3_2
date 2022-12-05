

class Product:
    """This class describes a product"""

    def __init__ (self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def calc_product_total(self, quantity):
        return float(self.price*quantity)

    def __eq__(self, other):
        if self.name == other.name and self.price == other.price:
            return True
        return False


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

    def add_to_cart(self, product: Product, quantity: int):
        """Adds  a product to the cart and adds the quantity to the quantity_cart."""
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
        for p in other.cart:
            if p in joined_cart.cart:
                index_other = other.cart.index(p)
                index_joined_cart = joined_cart.cart.index(p)
                joined_cart.quantity_cart[index_joined_cart] += other.quantity_cart[index_other]
            else:
                index_other = other.cart.index(p)
                joined_cart.cart.append(p)
                joined_cart.quantity_cart.append(other.quantity_cart[index_other])
        return joined_cart









apple = Product("apple", 30)
orange = Product("orange",50)

cart_1 = ShoppingCart()
cart_2 = ShoppingCart()

cart_2.add_to_cart(orange, 2)

cart_1.add_to_cart(orange, 4)
cart_1.add_to_cart(apple, 2)

our_cart = cart_1 + cart_2
print(our_cart.quantity_cart)
for p in our_cart.cart:
    print(p.name)
print(our_cart.calc_total())

