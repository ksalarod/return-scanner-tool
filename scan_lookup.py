from test_data import items

def scan_item():
barcode = input("Scan or enter item barcode: ")

if barcode in items:
item = items[barcode]
print(f"Item found: {item['name']} (SKU: {item['sku']})")
else:
print("Item not found. Please check the barcode.")

if __name__ == "__main__":
scan_item()
