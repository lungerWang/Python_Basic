class ShopCart(object):

    instance = None

    def __init__(self):

        print("初始化")

    def __new__(cls, *args, **kwargs):
        if ShopCart.instance is  None:
         ShopCart.instance = super().__new__(cls)
        return ShopCart.instance


cart1 = ShopCart()
cart2 = ShopCart()

print(cart1)
print(cart2)
