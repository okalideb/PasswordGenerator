import string
import secrets
import random
import time   

def get_yes_no(prompt):
    """Prompt the user with a yes/no question and return True or False."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")

def get_length(prompt):
    """Prompt the user for a positive integer length and return it."""
    while True:
        val = input(f"{prompt}: ").strip()
        if not val.isdigit():
            print("Please enter a positive integer.")
            continue
        length = int(val)
        if length <= 0:
            print("Length must be greater than zero.")
            continue
        return length

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    """
    Generate a secure password with given traits using secrets module.
    Ensures each selected type appears at least once by pre-picking required chars,
    then filling the rest and shuffling.
    """
    charset = ''
    required = []

    if use_lower:
        charset += string.ascii_lowercase
        required.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        charset += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        charset += string.digits
        required.append(secrets.choice(string.digits))
    if use_special:
        charset += string.punctuation
        required.append(secrets.choice(string.punctuation))

    if not charset:
        raise ValueError("At least one character type must be selected.")
    if length < len(required):
        raise ValueError(
            f"Password length must be at least {len(required)} to include each selected character type."
        )

    # Fill the remaining characters
    remaining = [secrets.choice(charset) for _ in range(length - len(required))]
    # Combine required chars with random picks
    password_chars = required + remaining
    # Securely shuffle to avoid predictable required-placement
    random.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

def main():
    print("ヽ(=^･ω･^=)丿  Welcome to the Secure Password Generator!  乁(=^･ω･^=)ノ")
    print("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    print("Developer note: A secure password must be as diverse and as long as possible. We recommend a password of length no less than 8 characters❗")
    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

    while True:  # Outer loop for multiple password generations
        # Inner loop to handle retries on invalid input
        while True:
            try:
                length = get_length("Enter desired password length")
                use_lower = get_yes_no("Include lowercase letters?")
                use_upper = get_yes_no("Include uppercase letters?")
                use_digits = get_yes_no("Include digits?")
                use_special = get_yes_no("Include special characters (e.g. !@#$)?")
                
                pwd = generate_password(length, use_lower, use_upper, use_digits, use_special)
                
                # Password generation animation
                print("\n⋘ please wait... ⋙\n")
                print("Generating password ✍️")
                time.sleep(0.3)
                print("■□□□□20%")
                time.sleep(0.3)
                print("■■■□□60%")
                time.sleep(0.3)
                print("■■■■□80%")
                time.sleep(0.3)
                print("■■■■■100%\n")
                print(f"Generated password (づ ᴗ _ᴗ)づ: {pwd}\n")
                break  # Exit inner loop on successful generation
            except ValueError as e:
                print(f"Error: {e}")
                print("Let's try again!\n")

        # Ask if user wants to generate another password
        if not get_yes_no("Generate another password?"):
            print("Goodbye! Have a secure day! (=^･ω･^=)")
            break

if __name__ == "__main__":
    main()
