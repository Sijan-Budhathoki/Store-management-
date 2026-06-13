import datetime

def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
#asking the require fields 
def sales_invoice():
    name = input("Customer name: ")
    filename = f"sales_invoice_{name}_{get_now()}.txt"
    total = 0
    lines = [f"Sales Invoice", f"Customer: {name}", f"Date: {get_now()}\n"]

    while True:
        product = input("Product name (or 'done'): ")
        if product.lower() == 'done':
            break
        brand = input("Brand: ")
        qty = int(input("Quantity: "))
        price = float(input("Price per item (Rs): "))
        free = qty // 3
        subtotal = qty * price
        total += subtotal
        lines.append(f"{product} ({brand}) - Qty: {qty} (+{free} free) - Rs {subtotal:.2f}")

    lines.append(f"\nTotal: Rs {total:.2f}")
    content = "\n".join(lines)

    print("\n" + content)
    with open(filename, "w") as f:
        f.write(content)
    print("\nInvoice saved as:" +filename)

def restock_invoice():
    name = input("Supplier name: ")
    filename = f"restock_invoice_{name}_{get_now()}.txt"
    total = 0
    lines = [f"Restock Invoice", f"Supplier: {name}", f"Date: {get_now()}\n"]

    while True:
        product = input("Product name (or 'done'): ")
        if product.lower() == 'done':
            break
        brand = input("Brand: ")
        qty = int(input("Quantity: "))
        price = float(input("Cost price (Rs): "))
        subtotal = qty * price
        total += subtotal
        lines.append(f"{product} ({brand}) - Qty: {qty} - Rs {subtotal:.2f}")

    lines.append(f"\nTotal: Rs {total:.2f}")
    content = "\n".join(lines)

    print("\n" + content)
    with open(filename, "w") as f:
        f.write(content)
    print("\nInvoice saved as:" + filename)

# formindg a manue 
if __name__ == "__main__":
    print("1. Sales Invoice")
    print("2. Restock Invoice")
    option = input("Choose (1 or 2): ")

    if option == '1':
        sales_invoice()
    elif option == '2':
        restock_invoice()
    else:
        print("Invalid choice.")
