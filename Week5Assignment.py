# File Creation
with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("12345\n")
    file.write("Another line here.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is appended line 1.\n")
        file.write("67890\n")
        file.write("Another appended line.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending completed.")
