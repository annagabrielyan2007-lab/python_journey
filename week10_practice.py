# WEEK 10: Introduction to Object-Oriented Programming (Classes & Objects)

class UserProfile:
    """A class representing a user profile with data and methods."""
    
    def __init__(self, name, role):
        """Initializes the user profile attributes."""
        self.name = name
        self.role = role
        self.completed_weeks = [5, 6, 7, 8, 9]
        
    def display_info(self):
        """Prints out the user profile details."""
        print(f"--- User Profile ---")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Completed Weeks: {self.completed_weeks}")
        print("--------------------")
        
    def add_completed_week(self, week_number):
        """Adds a new completed week to the profile."""
        if week_number not in self.completed_weeks:
            self.completed_weeks.append(week_number)
            print(f"Added Week {week_number} to completed list!")
        else:
            print(f"Week {week_number} is already listed.")

if __name__ == "__main__":
    print("--- WEEK 10: OBJECT-ORIENTED PROGRAMMING LAB ---\n")
    
    # Create an instance of UserProfile
    my_profile = UserProfile("Alex", "Python Developer in Training")
    
    # 1. Display initial profile info
    my_profile.display_info()
    print()
    
    # 2. Update state by adding Week 10
    my_profile.add_completed_week(10)
    print()
    
    # 3. Display updated info
    my_profile.display_info()