import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Function to encrypt data using AES-GCM
def encrypt_data(plaintext):
    key = os.urandom(32)  # 256-bit key
    nonce = os.urandom(12)  # 96-bit nonce
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    # Return key, nonce, ciphertext, and tag
    return (key, nonce, ciphertext, encryptor.tag)

# Function to validate edge data
def validate_edge_data(data):
    if "<script>" in data or "DROP TABLE" in data.upper():
        raise ValueError("Potential malicious content detected!")
    return data

# A mock function to simulate access control
def check_access(user_role, slice_required_role):
    # Simulating access control for different slices
    slices = {
        "admin": ["low_latency", "high_throughput", "massive_IoT"],
        "user": ["low_latency", "high_throughput"],
        "guest": ["massive_IoT"]
    }
    
    if slice_required_role in slices.get(user_role, []):
        return f"Access granted to {slice_required_role} network slice."
    else:
        return f"Access denied. Insufficient permissions for {slice_required_role} slice."

# Function to handle encryption
def handle_encryption():
    plaintext = entry_plaintext.get()
    if plaintext:
        key, nonce, ciphertext, tag = encrypt_data(plaintext)
        # Convert ciphertext to hex for better readability
        encrypted_data = ciphertext.hex()
        result_text.set(f"Encrypted data: {encrypted_data}")
    else:
        messagebox.showerror("Input Error", "Please enter data to encrypt.")

# Function to handle edge data validation
def handle_edge_validation():
    user_input = entry_edge_data.get()
    try:
        safe_data = validate_edge_data(user_input)
        result_edge.set(f"Data is safe for processing: {safe_data}")
    except ValueError as e:
        result_edge.set(f"Error: {str(e)}")

# Function to handle access control
def handle_access_control():
    user_role = entry_role.get()
    slice_required_role = entry_slice.get()  # Allow user to input slice type
    access_message = check_access(user_role, slice_required_role)
    result_access.set(access_message)

# Create the main window
window = tk.Tk()
window.title("6G Network Security")

# Create and pack labels, entries, and buttons for encryption
label_plaintext = tk.Label(window, text="Enter the data to be encrypted:")
label_plaintext.pack(pady=5)

entry_plaintext = tk.Entry(window, width=40)
entry_plaintext.pack(pady=5)

encrypt_button = tk.Button(window, text="Encrypt Data", command=handle_encryption)
encrypt_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=5)

# Create and pack labels, entries, and buttons for edge data validation
label_edge_data = tk.Label(window, text="Enter data for edge processing:")
label_edge_data.pack(pady=5)

entry_edge_data = tk.Entry(window, width=40)
entry_edge_data.pack(pady=5)

validate_button = tk.Button(window, text="Validate Edge Data", command=handle_edge_validation)
validate_button.pack(pady=10)

result_edge = tk.StringVar()
result_edge_label = tk.Label(window, textvariable=result_edge)
result_edge_label.pack(pady=5)

# Create and pack labels, entries, and buttons for access control
label_role = tk.Label(window, text="Enter your role (admin/user/guest):")
label_role.pack(pady=5)

entry_role = tk.Entry(window, width=40)
entry_role.pack(pady=5)

label_slice = tk.Label(window, text="Enter the network slice (low_latency/high_throughput/massive_IoT):")
label_slice.pack(pady=5)

entry_slice = tk.Entry(window, width=40)
entry_slice.pack(pady=5)

access_button = tk.Button(window, text="Check Access", command=handle_access_control)
access_button.pack(pady=10)

result_access = tk.StringVar()
result_access_label = tk.Label(window, textvariable=result_access)
result_access_label.pack(pady=5)

# Run the main loop of the window
window.mainloop()
