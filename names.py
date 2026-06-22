def main():
    name = input("Name: ")

    # the "with" block will automatically close the file because its a context manager.
    # "w" = write. the "w" mode is dangerous because will recreate the file every time.
    # "a" = append. Will add the content at the end of the file.
    with open("names.txt", "a") as f:
        f.write(f"{name}\n")
    with open("names.txt") as file:
        # You can iterate inside a files content with for loops like this:
        for line in sorted(
            file, reverse=True
        ):  # Telling that I want to sort the file in a reverse order
            print(line.rstrip())  # Right remove the \n from the line


if __name__ == "__main__":
    main()
