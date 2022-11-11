# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    def __init__(self, name):
        self.name = name
        self.shop_cart = {}
        self.number_of_items = 0
        
    def add_item(self):
        name = input('What item would you like to add?')
        self.shop_cart[name] = name
        self.number_of_items +=1
        print(f'{name} was added to the shopping cart')
        
    def remove_item(self):
        name = input('What item would you like to remove')
        if name in self.shop_cart:
                print(f' The {name} was removed from the shopping cart')
                del self.shop_cart[name]
                self.number_of_items -=1
        else:
            print('Item is not in the shopping cart')
        
    def show_item(self):
        print('the current item in your shopping cart is')
        print(f'number of items: {self.number_of_items}')
        for k,v in self.shop_cart.items():
            print(k,v)
            
    def runner(self):
        while True:
            customer_choice = input('What would you like to do? (add,remove,show or quit)')
            if customer_choice == 'add':
                self.add_item()
            elif customer_choice == 'remove':
                self.remove_item()
            elif customer_choice == 'show':
                self.show_item() 
            elif customer_choice == 'quit':
                self.show_item()
                print('Thanks for shopping with us')
                break
            else:
                print('Invalid choice, please try again.')
        
customer = Cart('customer')

customer.runner()


