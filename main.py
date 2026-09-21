from pathlib import Path

from models.product import Product
from services.inventory import Inventory
from storage.json_storage import JsonStorage


def display_products(products):
	if not products:
		print("No products found.")
		return

	for product in products:
		print(
			f"{product.product_id}: {product.name} | "
			f"Price: {product.price} | Category: {product.category} | "
			f"Quantity: {product.quantity}"
		)


def add_product(inventory):
	product = Product(
		name=input("Name: ").strip(),
		product_id=input("Product ID: ").strip(),
		price=float(input("Price: ")),
		category=input("Category: ").strip(),
		quantity=int(input("Quantity: ")),
		minimum_stock=int(input("Minimum stock: ")),
	)
	inventory.add_product(product)
	print("Product added.")


def update_product(inventory):
	product_id = input("Product ID to update: ").strip()
	product = inventory.find_product(product_id)
	if product is None:
		print("Product not found.")
		return

	print("Press Enter to keep the current value.")
	changes = {}
	for field in ("name", "price", "category", "quantity", "minimum_stock"):
		value = input(f"{field} [{getattr(product, field)}]: ").strip()
		if value:
			changes[field] = float(value) if field == "price" else (
				int(value) if field in {"quantity", "minimum_stock"} else value
			)

	inventory.update_product(product_id, **changes)
	print("Product updated.")


def run():
	inventory = Inventory(JsonStorage(Path(__file__).parent / "products.json"))

	while True:
		print("\nInventory Management")
		print("1. Add product")
		print("2. View all products")
		print("3. Search for a product")
		print("4. Update product")
		print("5. Remove product")
		print("6. Exit")
		choice = input("Choose an option: ").strip()

		try:
			if choice == "1":
				add_product(inventory)
			elif choice == "2":
				display_products(inventory.get_all_products())
			elif choice == "3":
				display_products(inventory.search_products(input("Search: ").strip()))
			elif choice == "4":
				update_product(inventory)
			elif choice == "5":
				product_id = input("Product ID to remove: ").strip()
				print("Product removed." if inventory.remove_product(product_id) else "Product not found.")
			elif choice == "6":
				print("Goodbye.")
				break
			else:
				print("Invalid option.")
		except (ValueError, TypeError) as error:
			print(f"Error: {error}")


if __name__ == "__main__":
	run()
