class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_item(self):
        return self.name
    
    def update_price(self):
        new_price = float(input("Enter new price: "))
        if new_price > 0:
            self.price = new_price
            return self.price   
        else:   
            print("Invalid")    

    def update_quantity(self):
        new_quantity = int(input("How many items do you want to add or remove: "))
        print(f"Updated quantity: {new_quantity}")
        new_quantity = new_quantity + self.quantity

        if new_quantity >= 0:
            self.quantity = new_quantity
            return self.quantity
        else:
            return "Quantity cannot be negative"