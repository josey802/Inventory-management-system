from models.product import Product


class Inventory:
	PRODUCT_FIELDS = {
		"name",
		"product_id",
		"price",
		"category",
		"quantity",
		"minimum_stock",
	}

	def __init__(self, storage):
		self.storage = storage
		self.products = [Product(**record) for record in storage.load()]

	def _save(self):
		self.storage.save([product.__dict__ for product in self.products])

	def add_product(self, product):
		if self.find_product(product.product_id):
			raise ValueError("A product with this ID already exists.")

		self.products.append(product)
		self._save()

	def get_all_products(self):
		return list(self.products)

	def find_product(self, product_id):
		return next(
			(product for product in self.products if product.product_id == product_id),
			None,
		)

	def search_products(self, query):
		query = query.lower()
		return [
			product
			for product in self.products
			if query in product.product_id.lower()
			or query in product.name.lower()
			or query in product.category.lower()
		]

	def update_product(self, product_id, **changes):
		product = self.find_product(product_id)
		if product is None:
			raise ValueError("Product not found.")

		unknown_fields = set(changes) - self.PRODUCT_FIELDS
		if unknown_fields:
			raise ValueError(f"Unknown product fields: {', '.join(sorted(unknown_fields))}")

		if "product_id" in changes and changes["product_id"] != product_id:
			if self.find_product(changes["product_id"]):
				raise ValueError("A product with this ID already exists.")

		for field, value in changes.items():
			setattr(product, field, value)
		self._save()
		return product

	def remove_product(self, product_id):
		product = self.find_product(product_id)
		if product is None:
			return False

		self.products.remove(product)
		self._save()
		return True
