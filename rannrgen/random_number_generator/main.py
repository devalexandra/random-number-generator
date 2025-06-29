import random

def generate_random_nr():
    print("Generating a random number . . .")
    return random.randint(1, 10000)

def main():
    random_number = generate_random_nr()
    print(f"Random number generated: {random_number}")

if __name__ == "__main__":
    main()
