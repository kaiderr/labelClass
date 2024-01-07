class Label:
    # write to file
    # ask user for input
    @classmethod
    def write_file(cls):
        with open("temp.txt", 'w') as file:
            print("Please enter the following information:")
            file.write(input("First name: ") + ' ')
            file.write(input("Middle initial: ") + ' ')
            file.write(input("Last name: ") + '\n')
            file.write(input("Street address: ") + ' ')
            file.write(input("Street address continued (if none, hit enter): ") + '\n')
            file.write(input("City: ") + ', ')
            file.write(input("State: ") + ' ')
            file.write(input("Zip code: ") + '\n')
            file.write(input("Phone number: "))

    # display result
    @classmethod
    def display(cls):
        with open("temp.txt", 'r') as file:
            for line in file:
                print(line)

# calling methods
def main():
    newLabel = Label().write_file()
    readLabel = Label().display()

main()
