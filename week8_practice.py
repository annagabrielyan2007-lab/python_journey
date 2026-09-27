# WEEK 8: File I/O (Reading and Writing Files)

def write_user_notes(filename, note_content):
    """Writes or appends a note to a text file."""
    # Using 'a' mode (append) adds new text without erasing old text
    with open(filename, "a") as file:
        file.write(note_content + "\n")
    print(f"Successfully saved note to {filename}!")

def read_user_notes(filename):
    """Reads and prints the contents of a text file safely."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n--- Contents of {filename} ---")
            print(content.strip())
            print("-----------------------------------")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    print("--- WEEK 8: FILE I/O LAB ---\n")
    
    target_file = "my_notes.txt"
    
    # 1. Write some notes to our file
    write_user_notes(target_file, "Learned how to use try/except blocks in Week 7.")
    write_user_notes(target_file, "Starting Week 8: File handling in Python!")
    
    # 2. Read the notes back from the file
    read_user_notes(target_file)