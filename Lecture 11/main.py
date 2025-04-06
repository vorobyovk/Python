import pickle
import json
import copy

# def write_contacts_to_file(filename, contacts):
#     try:
#         with open(filename, 'wb') as f:
#             pickle.dump(contacts, f)
#         print(f"Contacts successfully written to {filename}")
#     except Exception as e:
#         print(f"Error writing contacts to file: {e}")
# def read_contacts_from_file(filename):
#     try:
#         with open(filename, 'rb') as f:
#             contacts = pickle.load(f)
#         print(f"Contacts successfully read from {filename}")
#         return contacts
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return []
#     except Exception as e:
#         print(f"Error reading contacts from file: {e}")
#         return []
# if __name__ == '__main__':    
#     contacts_data = [
#         {
#             "name": "Allen Raymond",
#             "email": "nulla.ante@vestibul.co.uk",
#             "phone": "(992) 914-3792",
#             "favorite": False,
#         },
#         {
#             "name": "Ricardo Tubbs",
#             "email": "rtubbs@miamivice.com",
#             "phone": "555-123-4567",
#             "favorite": True,
#         },
#     ]
#     filename = "contacts.pkl"
#     write_contacts_to_file(filename, contacts_data)
#     loaded_contacts = read_contacts_from_file(filename)
#     if loaded_contacts:
#         print("\nLoaded Contacts:")
#         for contact in loaded_contacts:
#             print(contact)

# def write_data_to_json_file(filename, data):
#     try:
#         with open(filename, "w") as file:
#             json.dump(data, file, indent=2)  # Use indent for pretty-printing
#         print(f"Data successfully written to {filename}")
#     except (IOError, TypeError) as e:
#         print(f"Error writing data to file: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# def read_data_from_json_file(filename):
#     try:
#         with open(filename, "r") as file:
#             data = json.load(file)
#         print(f"Data successfully read from {filename}")
#         return data
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None
#     except (IOError, json.JSONDecodeError) as e:
#         print(f"Error reading data from file: {e}")
#         return None
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return None

# # Example Usage
# if __name__ == "__main__":
#     sample_data = {
#         "key": "value",
#         2: [1, 2, 3],
#         "tuple": (5, 6),
#         "a": {"key": "value"},
#         "boolean": True,
#         "none_value": None,
#     }
#     file_name = "data.json"
#     write_data_to_json_file(file_name, sample_data)
#     loaded_data = read_data_from_json_file(file_name)
#     if loaded_data:
#         print("\nLoaded Data:")
#         print(loaded_data)
#         # Demonstrate type conversions
#         print("\nType Conversion Demonstrations:")
#         print(f"Original data type of '2' key: {type(sample_data[2])}")
#         print(f"Loaded data type of '2' key: {type(loaded_data['2'])}")
#         print(f"Original data type of 'tuple' key: {type(sample_data['tuple'])}")
#         print(f"Loaded data type of 'tuple' key: {type(loaded_data['tuple'])}")
#         print(f"Original data type of 'boolean' key: {type(sample_data['boolean'])}")
#         print(f"Loaded data type of 'boolean' key: {type(loaded_data['boolean'])}")
#         print(f"Original data type of 'none_value' key: {type(sample_data['none_value'])}")
#         print(f"Loaded data type of 'none_value' key: {type(loaded_data['none_value'])}")
#         print(f"Original data type of key 2: {type(list(sample_data.keys())[1])}")
#         print(f"Loaded data type of key 2: {type(list(loaded_data.keys())[1])}")

class MyClass:
    def __init__(self, value):
        self.value = value
    def __copy__(self):
        print("Викликано __copy__")
        return MyClass(self.value)
    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))
# Поверхневе копіювання
obj = MyClass(5)
obj_copy = copy.copy(obj)
obj_copy.value = 10
# Глибоке копіювання
obj_deepcopy = copy.deepcopy(obj)
obj_deepcopy.value = 20
print(obj.value, obj_copy.value, obj_deepcopy.value)

