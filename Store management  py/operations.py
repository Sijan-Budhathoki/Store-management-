import datetime
import csv

STOCK_FILE = "stock.txt"

def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

def load_stock():
    stock = {}
    try:
        with open(STOCK_FILE, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row['product'].lower(), row['brand'].lower())
                stock[key] = {
                    'product': row['product'],
                    'brand': row['brand'],
                    'quantity': int(row['quantity']),
                    'price': float(row['price'])
                }
    except FileNotFoundError:
        with open(STOCK_FILE, 'w') as f:
            f.write("product,brand,quantity,price\n")
    except Exception as e:
        print("Error loading stock:", e)
    return stock

def save_stock(stock):
    try:
        with open(STOCK_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['product', 'brand', 'quantity', 'price'])
            writer.writeheader()
            for item in stock.values():
                writer.writerow(item)
    except Exception as e:
        print("Error saving stock:", e)

def show_products():
    stock = load_stock()
    if not stock:
        print("Stock is empty.")
        return
    print("\nCurrent Stock:\n")
    print("Product        Brand          Qty        Price (Rs)")
    print("-" * 50)
    for item in stock.values():
        print(f"{item['product']:15} {item['brand']:15} {item['quantity']:10} {item['price']:10.2f}")

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_number(value):
    try:
        val = float(value)
        return val >= 0
    except:
        return False

def sales_invoice():
    stock = load_stock()

    while True:
        name = input("Customer name: ").strip()
        if is_valid_name(name):
            break
        else:
            print("Invalid customer name. Use only letters and spaces.")

    filename = "sales_invoice_" + name + "_" + get_now() + ".txt"
    total = 0
    lines = ["Sales Invoice", "Customer: " + name, "Date: " + get_now() + "\n"]

    while True:
        try:
            product = input("Product name (or 'done'): ").strip()
            if product.lower() == 'done':
                break
            if not is_valid_name(product):
                print("Invalid product name.")
                continue

            brand = input("Brand: ").strip()
            if not is_valid_name(brand):
                print("Invalid brand name.")
                continue

            key = (product.lower(), brand.lower())
            if key not in stock:
                print("Product not found in stock.")
                continue

            available = stock[key]['quantity']
            print("Available: ", available)

            qty_input = input("Quantity to sell: ")
            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("Invalid or negative quantity.")
                continue

            qty = int(qty_input)
            if qty > available:
                print("Not enough stock.")
                continue

            price = stock[key]['price']
            free = qty // 3
            subtotal = qty * price
            total += subtotal

            print(f"Deducting {qty} from stock. Before: {available}, After: {available - qty}")
            stock[key]['quantity'] -= qty

            lines.append(f"{product} ({brand}) - Qty: {qty} (+{free} free) - Rs {subtotal:.2f}")
#adding the cryteria for the data entered
        except Exception as e:
            print("Error during sales entry:", e)

    lines.append("\nTotal: Rs {:.2f}".format(total))
    content = "\n".join(lines)

    print("\n" + content)
    try:
        with open(filename, "w") as f:
            f.write(content)
        print("Invoice saved as:", filename)
    except Exception as e:
        print("Error saving invoice:", e)

    save_stock(stock)

def restock_invoice():
    stock = load_stock()

    while True:
        name = input("Supplier name: ").strip()
        if is_valid_name(name):
            break
        else:
            print("Invalid supplier name.")

    filename = "restock_invoice_" + name + "_" + get_now() + ".txt"
    total = 0
    lines = ["Restock Invoice", "Supplier: " + name, "Date: " + get_now() + "\n"]

    while True:
        try:
            product = input("Product name (or 'done'): ").strip()
            if product.lower() == 'done':
                break
            if not is_valid_name(product):
                print("Invalid product name.")
                continue

            brand = input("Brand: ").strip()
            if not is_valid_name(brand):
                print("Invalid brand name.")
                continue

            qty_input = input("Quantity to restock: ")
            price_input = input("Cost price (Rs): ")

            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("Invalid or negative quantity.")
                continue
            if not is_valid_number(price_input):
                print("Invalid or negative price.")
                continue

            qty = int(qty_input)
            price = float(price_input)
            key = (product.lower(), brand.lower())

            if key in stock:
                before_qty = stock[key]['quantity']
                stock[key]['quantity'] += qty
                stock[key]['price'] = price
                print(f"Adding {qty} to stock. Before: {before_qty}, After: {stock[key]['quantity']}")
            else:
                stock[key] = {
                    'product': product,
                    'brand': brand,
                    'quantity': qty,
                    'price': price
                }
                print(f"New item added to stock with quantity {qty}.")

            subtotal = qty * price
            total += subtotal
            lines.append(f"{product} ({brand}) - Qty: {qty} - Rs {subtotal:.2f}")

        except Exception as e:
            print("Error during restocking:", e)

    lines.append("\nTotal: Rs {:.2f}".format(total))
    content = "\n".join(lines)

    print("\n" + content)
    try:
        with open(filename, "w") as f:
            f.write(content)
        print("Invoice saved as:", filename)
    except Exception as e:
        print("Error saving invoice:", e)

    save_stock(stock)

def sell_product():
    try:
        sales_invoice()
    except Exception as e:
        print("Error in sell_product:", e)

def restock_product():
    try:
        restock_invoice()
    except Exception as e:
        print("Error in restock_product:", e)
