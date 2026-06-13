def load_products():
    try:
        with open("products.txt", "r") as f:
            products = []
            for line in f:
                parts = line.split(',') 
                if len(parts) == 4:  
                    products.append({
                        'id': parts[0],
                        'name': parts[1],
                        'country': parts[2],
                        'brand': parts[3],
                        'price': 0.0,
                        'quantity': 0
                    })
            return products
    except FileNotFoundError:
        print("products file not found")
        return []
    except ValueError:
        print("Error in file format")
        return []
#if the product is not available
def show_products(products):
    if not products:
        print("No products available")
        return

    print("\n   ID   Name               Country            Brand           Quantity          Price  ")
    print("-" * 50)

    for p in products:
        line = p['id'].ljust(4) + " " + p['name'].ljust(18) + " " + p['country'].ljust(21) + " " + p['brand']
        print(line)

    print("-" * 50)
    print("Total: " + str(len(products)) + " products")

if __name__ == "__main__":
    show_products(load_products())
