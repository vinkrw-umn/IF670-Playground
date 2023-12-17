import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 16  # You can change the length here
    random_password = generate_password(password_length)
    print(f"Randomly generated password: {random_password}")
