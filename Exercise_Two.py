class Fruits():
    def __init__(self, color, size):
        self.color = color
        self.size = size
        
        
    def first_get(self):
        color = input('Please enter a command')
        size = input('Please enter the same command').upper()
        print(f'{size}')
        
        
apple = Fruits('red', 'small')    

apple.first_get()