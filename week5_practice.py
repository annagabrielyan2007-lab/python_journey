#week5_practice.py - Advanced String Manuipualion & Text Parsing

def clean_and_phrase_data():
    # 1. Messy raw input data (typical real-world scenario)
    raw_input_data = "[ERROR]: User_ID_9482 failed to authenticate. IP: 192.168.1.50  "

    # 2. Stripping whitespace 
    cleaned_string = raw_input_data.strip()
    print(f"Cleaned: '{cleaned_string}")

    # 3. Splitting text into a list of words/tokens
    tokens = cleaned_string.split(" ")
    print(f"Tokens List:  {tokens}")

    # 4. Ectracting specific components (Text Parsing)
    log_level = cleaned_string.split("]:")[0].replace("[", "")
    user_info = cleaned_string.split("User_ID_")[1].split(" ")[0]

    print(f"Parsed Log Level: {log_level}")
    print (f"Parsed User ID: {user_info}")

    # 5. Joining strings back together with a custom separator 
    tag_list = ["python", "development", "backend", "automation"]
    hashtag_string = " #".join(tag_list)
    print(f"Formatted Tags: #{hashtag_string}")

    if __name__ == "__main__"
    print("=== WEEK 5: STRING MANIPULAYION LAB ===\n")
    clean_and_phrase_data()