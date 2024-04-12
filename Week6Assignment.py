try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: This is a mix of strings and numbers.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Another string here.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File creation completed.")

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

try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: This is an appended line.\n")
        file.write("Line 5: 67890\n")
        file.write("Line 6: Another appended line.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending completed.")
