import json
from pathlib import Path


class JsonStorage:
	def __init__(self, file_path):
		self.file_path = Path(file_path)

	def load(self):
		if not self.file_path.exists():
			return []

		with self.file_path.open("r", encoding="utf-8") as file:
			return json.load(file)

	def save(self, records):
		self.file_path.parent.mkdir(parents=True, exist_ok=True)
		with self.file_path.open("w", encoding="utf-8") as file:
			json.dump(records, file, indent=2)
