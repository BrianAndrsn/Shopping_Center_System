# =============================================================================================================================================#

# =============================================================================================================================================#
class Product:
    def __init__(self, sku, name, description, price, quantity, category):
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category = category

class ElectronicsProduct(Product):
    def __init__(self, sku, name, description, price, quantity, category, warranty_period):
        super().__init__(sku, name, description, price, quantity, category)
        self.warranty_period = warranty_period

    def check_warranty(self):
        if self.warranty_period > 0:
            return True
        else:
            return False

class ClothingProduct(Product):
    def __init__(self, sku, name, description, price, quantity, category, size):
        super().__init__(sku, name, description, price, quantity, category)
        self.size = size

    def get_size(self):
        return self.size

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
        
    def calculate_total(self):
        total = sum(map(lambda product: product.price * product.quantity, self.products))
        return total

    # def calculate_total(self):
    #     total = 0
    #     for product in self.products:
    #         total += product.price * product.quantity
    #     return total

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_product(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_product(product)

    def view_cart(self):
        if len(self.shopping_cart.products) == 0:
            print("Your shopping cart is empty.")
        else:
            print("Your shopping cart contains the following products:")
            for product in self.shopping_cart.products:
                print(f"- {product.name}, quantity: {product.quantity}, price: ${product.price}")

    def checkout(self, payment_info):
        if len(self.shopping_cart.products) == 0:
            print("Your shopping cart is empty. Please add some products before checking out.")
        else:
            total = self.shopping_cart.calculate_total()
            print(f"Your total cost is ${total}.")
            confirm = input("Do you want to proceed with the payment? (Y/N) ")
            if confirm.lower() == "y":
                # Process the payment using the provided payment_info
                # Reduce the quantity of each product in the shopping cart
                for product in self.shopping_cart.products:
                    product.quantity -= 1
                # Send a confirmation email to the customer
                print(f"Thank you for your purchase, {self.name}! We have sent a confirmation email to {self.email}.")
                # Clear the shopping cart
                self.shopping_cart.products = []
            else:
                print("Payment cancelled.")

def create_product():
    sku = input("Enter the SKU: ")
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the price: $"))
    quantity = int(input("Enter the quantity: "))
    category = input("Enter the category: ")
    return Product(sku, name, description, price, quantity, category)

def create_electronics_product():
    sku = input("Enter the SKU: ")
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the price: $"))
    quantity = int(input("Enter the quantity: "))
    category = input("Enter the category: ")
    warranty_period = int(input("Enter the warranty period (in months): "))
    return ElectronicsProduct(sku, name, description, price, quantity, category, warranty_period)

def create_clothing_product():
    sku = input("Enter the SKU: ")
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the price: $"))
    quantity = int(input("Enter the quantity: "))
    category = input("Enter the category: ")
    size = input("Enter the size: ")
    return ClothingProduct(sku, name, description, price, quantity, category, size)

def add_product_to_cart(customer):
    while True:
        choice = input("What type of product would you like to add? (P)roduct, (E)lectronics product, (C)lothing product, or (D)one? ")
        if choice.lower() == 'p':
            product = create_product()
            customer.add_to_cart(product)
        elif choice.lower() == 'e':
            product = create_electronics_product()
            customer.add_to_cart(product)
        elif choice.lower() == 'c':
            product = create_clothing_product()
            customer.add_to_cart(product)
        elif choice.lower() == 'd':
            break
        else:
            print("Invalid choice. Please try again.")

def remove_product_from_cart(customer):
    while True:
        if len(customer.shopping_cart.products) == 0:
            print("Your shopping cart is empty.")
            break
        else:
            print("Your shopping cart contains the following products:")
            for i, product in enumerate(customer.shopping_cart.products):
                print(f"{i+1}. {product.name}, quantity: {product.quantity}")
            choice = input("Which product would you like to remove? (Enter the number or type 'D' to exit): ")
            if choice.lower() == 'd':
                break
            else:
                try:
                    index = int(choice) - 1
                    product = customer.shopping_cart.products[index]
                    customer.remove_from_cart(product)
                    print(f"{product.name} has been removed from your shopping cart.")
                except:
                    print("Invalid choice. Please try again.")

def main():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    customer = Customer(name, email)

    while True:
        choice = input("What would you like to do? (A)dd a product to your cart, (R)emove a product from your cart, (V)iew your cart, (C)heck out or (Q)uit? ")
        if choice.lower() == 'a':
            add_product_to_cart(customer)
        elif choice.lower() == 'r':
            remove_product_from_cart(customer)
        elif choice.lower() == 'v':
            customer.view_cart()
        elif choice.lower() == 'c':
            payment_info = input("Enter your payment information: ")
            customer.checkout(payment_info)
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
# =============================================================================================================================================#

# =============================================================================================================================================#