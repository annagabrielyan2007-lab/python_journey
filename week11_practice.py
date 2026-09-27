# WEEK 11: Advanced Object-Oriented Programming (Inheritance)

class UserProfile:
    """Base class representing a general user profile."""
    
    def __init__(str_self, name, role):
        str_self.name = name
        str_self.role = role
        str_self.completed_weeks = [5, 6, 7, 8, 9, 10]
        
    def display_info(str_self):
        """Prints general user info."""
        print(f"Name: {str_self.name} | Role: {str_self.role}")
        print(f"Completed Weeks: {str_self.completed_weeks}")


class AdminProfile(UserProfile):
    """A specialized subclass of UserProfile with admin privileges."""
    
    def __init__(str_self, name, role, access_level):
        # super() calls the parent class (UserProfile) __init__ method
        super().__init__(name, role)
        str_self.access_level = access_level
        
    def display_info(str_self):
        """Overrides the parent display_info method to include admin details."""
        super().display_info()
        print(f"Access Level: Level {str_self.access_level} Admin")
        
    def manage_curriculum(str_self):
        """Admin-specific action."""
        print(f"Admin {str_self.name} is updating the curriculum structure.")


if __name__ == "__main__":
    print("--- WEEK 11: ADVANCED OOP & INHERITANCE LAB ---\n")
    
    # 1. Create a standard user profile
    print("1. Standard User:")
    base_user = UserProfile("Alex", "Python Developer in Training")
    base_user.display_info()
    
    print("\n2. Admin User (Using Inheritance):")
    # 2. Create an admin profile using inheritance
    admin_user = AdminProfile("Jordan", "Lead Instructor", access_level=5)
    admin_user.display_info()
    admin_user.manage_curriculum()