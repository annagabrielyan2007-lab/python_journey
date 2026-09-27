# WEEK 9: Structured Data (Dictionaries and JSON)
import json

def save_user_profile(filename, profile_data):
    """Saves a Python dictionary as a structured JSON file."""
    with open(filename, "w") as file:
        json.dump(profile_data, file, indent=4)
    print(f"Successfully saved structured profile to {filename}!")

def load_user_profile(filename):
    """Loads and reads structured data from a JSON file."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print(f"\n--- Loaded Profile from {filename} ---")
            print(f"Name: {data.get('name')}")
            print(f"Role: {data.get('role')}")
            print(f"Completed Weeks: {data.get('completed_weeks')}")
            print("---------------------------------------")
    except FileNotFoundError:
        print(f"Error: Profile file '{filename}' not found.")

if __name__ == "__main__":
    print("--- WEEK 9: STRUCTURED DATA LAB ---\n")
    
    target_file = "user_profile.json"
    
    # Our structured user profile data
    my_profile = {
        "name": "Alex",
        "role": "Python Developer in Training",
        "completed_weeks": [5, 6, 7, 8]
    }
    
    # 1. Save dictionary to a JSON file
    save_user_profile(target_file, my_profile)
    
    # 2. Load it back from the file and read it
    load_user_profile(target_file)