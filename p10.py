class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        total = 0
        for name, (qty, price) in self.items.items():
            total += qty * price
        return total

    def __len__(self):
        return len(self.items)


# Main Program 
inv = Inventory()

try:
    with open("stock.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                continue
            name, qty_str, price_str = parts
            try:
                qty = int(qty_str)
                price = int(price_str)
            except ValueError:
                print(f"Skipping {name}: bad number")
                continue
            inv.add_item(name, qty, price)
except FileNotFoundError:
    print("Error: 'stock.txt' file nahi mili! Pehle yeh file banao.")
    exit()

print(f"{len(inv)} items, total value {inv.total_value()}")

inv.remove_item("pen")
print(f"{len(inv)} items, total value {inv.total_value()}")

try:
    inv.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")