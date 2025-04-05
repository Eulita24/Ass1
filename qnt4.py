# Define the Dog class
class Dog:
    def make_sound(self):
        return "Woof! Woof!"

# Define the Cat class
class Cat:
    def make_sound(self):
        return "Meow! Meow!"

# Function that processes a sound object
def process_sound(sound_object):
    # Call the make_sound() method on the passed object
    print(sound_object.make_sound())

# Example usage
dog = Dog()
cat = Cat()

# Process sounds for both objects
process_sound(dog)  # Output: Woof! Woof!
process_sound(cat)  # Output: Meow! Meow!
