print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

array = [7, 29, 3, 17, 26, 1, 23, 8, 50, 19]


def menu():
    print("\n***~~~*~*~~*~*~*~*~*~~*~*~*******~*~*~~*~*~*~*~*~~*~*~~~***")
    print("                           Menu                            ")
    print("***~~~*~*~~*~*~*~*~*~~*~*~*******~*~*~~*~*~*~*~*~~*~*~~~***")
    print("\n||  1 Add an element                                   ||"
          "\n||  2 Insert an element                                ||"
          "\n||  3 Modify an element                                ||"
          "\n||  4 Delete an element                                ||"
          "\n||  5 Arrange in ascending order                       ||"
          "\n||  6 Arrange in descending order                      ||"
          "\n||  7 Identify the smallest number/element             ||"
          "\n||  8 Identify the largest number/element              ||"
          "\n||  9 Get the sum of all the elements                  ||"
          "\n||  10 Determine the length of the array               ||"
          "\n||  11 Get the number of times an element appeared     ||"
          "\n||  12 Exit                                            ||")


def append():
    add_num = int(input("Enter the element you want to add: "))
    array.append(add_num)
    print("The element has been added.")
    print("This is the new array: ", array)


def insert():
    ins_index = int(input("Enter the index you want to insert: "))
    ins_num = int(input("Enter the element you want to insert: "))
    array.insert(ins_index, ins_num)
    print("The element has been inserted.")
    print("This is the new array: ", array)


def modify():
    mod_index = int(input("Enter the index you want to modify: "))
    mod_num = int(input("Enter the element you want to modify: "))
    array[mod_index] = mod_num
    print("The element has been modified.")
    print("This is the new array: ", array)


def delete():
    del_index = int(input("Enter the index you want to delete: "))
    array.pop(del_index)
    print("The element has been deleted.")
    print("This is the new array: ", array)


def sort_asc():
    array.sort()
    print("The array has been arranged in ascending order.")
    print("This is the new array: ", array)


def sort_des():
    array.sort()
    array.reverse()
    print("The array has been arranged in descending order.")
    print("This is the new array: ", array)


def get_min():
    smallest = min(array)
    print("This is the smallest element in the array: ", smallest)


def get_max():
    largest = max(array)
    print("This is the largest element in the array: ", largest)


def get_sum():
    total = sum(array)
    print("This is the sum of all the elements in the array: ", total)


def get_len():
    length = len(array)
    print("This is the length of the array: ", length)


def get_count():
    num = int(input("Enter the number/element you want to count: "))
    counter = array.count(num)
    print("This is the number of times the element "f"{num} appeared: ", counter)


def exit_prog():
    print("Thank you for using this program. Goodbye!")
    exit()


while True:
    print("\nWELCOME!\nArray: ", array)
    menu()
    option = int(input("\nEnter the option you want to choose from the menu (1-12): "))
    if option == 1:
        append()
    elif option == 2:
        insert()
    elif option == 3:
        modify()
    elif option == 4:
        delete()
    elif option == 5:
        sort_asc()
    elif option == 6:
        sort_des()
    elif option == 7:
        get_min()
    elif option == 8:
        get_max()
    elif option == 9:
        get_sum()
    elif option == 10:
        get_len()
    elif option == 11:
        get_count()
    elif option == 12:
        exit_prog()
    else:
        print("Invalid option. Please choose between 1-12 only.")
