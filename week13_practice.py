# WEEK 13: Advanced OOP (Magic & Dunder Methods)

class UserProfile:
    """A class demonstrating magic/dunder methods for object representation and comparison."""
    
    def __init__(self, name, role, level):
        self.name = name
        self.role = role
        self.level = level
        
    def __str__(self):
        """Friendly string representation for end users (triggered by print())."""
        return f"{self.name} ({self.role}) - Level {self.level}"
        
    def __repr__(self):
        """Formal string representation for developers/debugging."""
        return f"UserProfile(name='{self.name}', role='{self.role}', level={self.level})"
        
    def __eq__(self, other):
        """Allows direct comparison between two UserProfile objects using '=='."""
        if isinstance(other, UserProfile):
            return self.level == other.level
        return False

if __name__ == "__main__":
    print("--- WEEK 13: MAGIC METHODS LAB ---\n")
    
    # 1. Creating user instances
    user1 = UserProfile("Alex", "Python Developer", 12)
    user2 = UserProfile("Jordan", "Lead Instructor", 15)
    user3 = UserProfile("Sam", "Junior Developer", 12)
    
    # 2. Testing __str__ (Printing objects directly)
    print("1. Testing __str__ (User-Friendly Display):")
    print(user1)  # Automatically calls the __str__ method!
    print(user2)
    print()
    
    # 3. Testing __repr__ (Developer representation)
    print("2. Testing __repr__ (Developer Representation):")
    print(repr(user1))
    print()
    
    # 4. Testing __eq__ (Operator Overloading)
    print("3. Testing __eq__ (Comparing Objects):")
    print(f"Does user1 have the same level as user2? {user1 == user2}")
    print(f"Does user1 have the same level as user3? {user1 == user3}")