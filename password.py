import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Length label and entry
        tk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.length_entry = tk.Entry(self.root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Include special characters checkbox
        self.include_special_chars = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Special Characters", variable=self.include_special_chars).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Generate button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Password display
        self.password_label = tk.Label(self.root, text="Generated Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.password_display = tk.Entry(self.root, width=50, font=('Arial', 14))
        self.password_display.grid(row=3, column=1, padx=10, pady=10)

    def generate_password(self):
        length = self.length_entry.get()
        try:
            length = int(length)
            if length < 8:
                tk.messagebox.showwarning("Input Error", "Password length should be at least 8 characters.")
                return

            use_special_chars = self.include_special_chars.get()
            password = self.create_password(length, use_special_chars)
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
        except ValueError:
            tk.messagebox.showwarning("Input Error", "Please enter a valid number for the password length.")

    def create_password(self, length, use_special_chars):
        # Define the character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation if use_special_chars else ""

        # Create the pool of characters to choose from
        all_chars = lower + upper + digits + special

        # Ensure the password contains at least one character from each character set
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits)
        ]
        
        if use_special_chars:
            password.append(random.choice(special))
        
        # Fill the rest of the password length with random characters
        password += [random.choice(all_chars) for _ in range(length - len(password))]

        # Shuffle the password list to ensure randomness
        random.shuffle(password)

        # Convert the list to a string
        return ''.join(password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
