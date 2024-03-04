import random

# Lists of first and last names
first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis"]

def generate_random_name():
    """Generate a random name."""
    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)
    return f"{random_first_name} {random_last_name}"

def main():
    """Main function to generate and print random names."""
    for _ in range(5):  # Generate and print 5 random names
        random_name = generate_random_name()
        print(random_name)

if __name__ == "__main__":
    main()
