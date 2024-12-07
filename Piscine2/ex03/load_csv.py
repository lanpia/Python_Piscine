import pandas as pd

def load(path: str) -> object:
	"""Load the data from a CSV file."""
	try:
		data = pd.read_csv(path)
		# print(f"Loading dataset of dimensions {data.shape}")
		return data
	except FileNotFoundError:
		print("Error: The file does not exist.")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
	return None