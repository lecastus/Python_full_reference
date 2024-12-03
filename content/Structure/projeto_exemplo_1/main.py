import shopping.shopping_cart
import utility

print(utility)
print(utility.multiply(2, 3))
print(utility.divide(2, 3))

# Uma pasta com modulos é um package
item = 'apple'
cart = shopping.shopping_cart.buy(item)
print(cart)
