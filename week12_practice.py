# WEEK 12: Advanced OOP (Encapsulation & Polymorphism)

class UserProfile:
    """Base class demonstrating encapsulation and polymorphism."""
    
    def __init__(self, name, role, email):
        self.name = name
        self.role = role
        # Encapsulation: Protected attribute (conventionally internal)
        self._email = email
        self._access_token = "SECURE_TOKEN_123"
        
    def get_email(self):
        """Getter method to safely access protected data."""
        return self._email
        
    def update_email(self, new_email):
        """Setter method to control how protected data is modified."""
        if "@" in new_email:
            self._email = new_email
            print(f"Email successfully updated to: {self._email}")
        else:
            print("Error: Invalid email format.")

    def get_dashboard_view(self):
        """Polymorphic method to be overridden by subclasses."""
        return f"Standard Dashboard for {self.name} ({self.role})"


class AdminProfile(UserProfile):
    """Subclass demonstrating polymorphism with custom dashboard views."""
    
    def get_dashboard_view(self):
        """Polymorphic override: Admin sees an administrative dashboard."""
        return f"ADMINISTRATIVE Dashboard for {self.name} [Access Level: Full Control]"


if __name__ == "__main__":
    print("--- WEEK 12: ENCAPSULATION & POLYMORPHISM LAB ---\n")
    
    # 1. Testing Encapsulation
    print("1. Testing Encapsulation (Getters and Setters):")
    user = UserProfile("Alex", "Developer", "alex@example.com")
    print(f"Current Email: {user.get_email()}")
    user.update_email("alex.new@example.com")
    print()
    
    # 2. Testing Polymorphism
    print("2. Testing Polymorphism (Unified Interface):")
    standard_user = UserProfile("Sam", "Student", "sam@example.com")
    admin_user = AdminProfile("Jordan", "Lead Instructor", "jordan@example.com")
    
    # We call the exact same method name (.get_dashboard_view()) on different objects!
    users_list = [standard_user, admin_user]
    
    for u in users_list:
        print(u.get_dashboard_view())