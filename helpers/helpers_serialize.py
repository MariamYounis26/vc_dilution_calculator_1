import pickle

def save_object(obj, filename: str) -> None:
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def load_object(filename: str):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def format_currency(amount: float) -> str:
        return f"${amount:,.2f}"
