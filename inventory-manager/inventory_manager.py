class InventoryManager: # Define class that manages items in inventory
    def __init__(self,  items=None): # Initialize with a list of items
        if items is None:   # If there is no item list
            self.items = [] # Start with an empty list
        else:   # Else
            self.items = items  # Use existing list

    def add_item(self): # Function to add item to item list
        item = input("What item do you want to add? ")  #   Ask user for item to add to list
        self.items.append(item) # Append item to item list
        print(f"{item} added successfully") # Priny item added successfully
    
    def display_items(self):    # Function to display items
        for item in self.items: # Loop through each item in the item list
            print(item) # Print item


manager = InventoryManager()
manager.add_item()
manager.add_item()
manager.display_items()