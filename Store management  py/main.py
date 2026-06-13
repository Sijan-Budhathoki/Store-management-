from read import load_products, show_products
from write import sales_invoice, restock_invoice
from operations import sell_product, restock_product
#accessing every thing 
def main():
    while True:
        print("\n--- WeCare ---")
        print("1. Show Products")
        print("2. Sell")
        print("3. Restock")
        print("4. Manual Sales Invoice")
        print("5. Manual Restock Invoice")
        print("6. Exit")

        c = input("Choose: ")

        if c == '1':
            show_products(load_products())  # smave visible the available 
        elif c == '2':
            sell_product()  # when the product is selled its updated
        elif c == '3':
            restock_product()  # same as above restocking and updating the stocks 
        elif c == '4':
            sales_invoice()  # creating invoices requiees for sales 
        elif c == '5':
            restock_invoice()  # same as sales generating the invoice for restock
        elif c == '6':
            break  # Exit the program
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
