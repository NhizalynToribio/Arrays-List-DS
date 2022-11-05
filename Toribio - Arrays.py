print("********* PROGRAMMED BY: **********")
print("****** TORIBIO, NHIZALYN P. *******")
print("********** BSCOE 2 - 2 ************")
print("****** LABORATORY EXERCISE ******\n")


print("This are the List of My Favorite Numbers: 11, 26, 31, 25, 15, 4, 27, 10, 3, 62")


def print_menu():
    print(
        """\n
        >>>>>>>>>>>>>>> HELLO WELCOME <<<<<<<<<<<<<<<
        --------------- ARRAY PROGRAM ----------------
        \nWhat would you like to do?
        1. -> Add an Element                     [1]
        2. -> Insert an Element                  [2]
        3. -> Modify an Element                  [3]
        4. -> Delete an Element                  [4]
        5. -> Arrange in Ascending order         [5]
        6. -> Arrange in Descending order        [6]
                   ADDITIONAL COMMANDS
        7. -> Find the Minimum Element           [7]
        8. -> Find the Maximum Element           [8]
        9. -> Find the Sum of all the Element    [9]
        10. -> Exit the Program.                 [10]

        """
    )


ListOfFaveNum = [11, 26, 31, 25, 15, 4, 27, 10, 3, 62]
Count = 0
Element = []
print_menu()

# This program will ask the user to choose on what to do.
while Count <= 100:
    Choice = input("\n>Hi! Please choose a number depending on what do you want to do? (1-10): ")

    # (1) This is the Add Element Section
    if Choice == "1":
        print("\n>>>>>>>>>>> ADD an ELEMENT <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        try:
            Element = int(input("\nPlease input an Element to be added: "))
        except ValueError:
            print("\nInvalid input")
        else:
            ListOfFaveNum.append(Element)
            print("\nYou have Successfully added a new Element.")
            print("This is the New Element ADDED:", Element)
            print("\nThis is the New Array: Fave Numbers:", ListOfFaveNum)
        print_menu()

    # (2) This is the Insert Element Section ----
    elif Choice == "2":
        print("\n>>>>>>>>>>> INSERT an ELEMENT <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        try:
            Index = int(input("\nPlease input an index number you want to insert the new element: "))
            Element = int(input("Please input the new element: "))
        except ValueError:
            print("\nInvalid input")
        else:
            ListOfFaveNum.insert(Index, Element)
            print("\nYou have Successfully Inserted a new Element.")
            print("This is the New Element Inserted:", Element)
            print("This is the new inserted array: Fave Numbers: ", ListOfFaveNum)
        print_menu()

    # (3) This is the Modify Element Section -----
    elif Choice == "3":
        print("\n>>>>>>>>>>> MODIFY an ELEMENT <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        try:
            Indexnum = int(input("\nPlease input the index you want to modify: "))
            NewElement = int(input("Please input an element you want to add: "))
        except ValueError:
            print("\nInvalid input")
        else:
            ListOfFaveNum[Indexnum] = NewElement
            print("\nYou have Successfully Modify an Element.")
            print("This is the New Element Modified:", NewElement)
            print("This is the new Modified array: Fave Numbers: ", ListOfFaveNum)
        print_menu()

    # (4) This is the Delete Element Section:
    elif Choice == "4":
        print("\n>>>>>>>>>>> DELETE an ELEMENT <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        try:
            Index = int(input("\nPlease input the index number you want to delete: "))
        except ValueError:
            print("\nInvalid input")
        else:
            ListOfFaveNum.remove(ListOfFaveNum[Index])
            print("\nYou have Successfully Deleted an Element.")
            print("This is the new array: Fave Numbers: ", ListOfFaveNum)
        print_menu()

    # (5) This is the Arranging the Element in Ascending Section:
    elif Choice == "5":
        print("\n>>>>>>>>>>> Ascending Arrangement of Element <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        ListOfFaveNum.sort()
        print("\nYou have Successfully Sorted the Elements in Ascending arrangement.")
        print("\nThis is the New Ascending Arrangement of Element:", ListOfFaveNum)
        print_menu()

    # (6) This is the Arranging the Element in Descending Section:
    elif Choice == "6":
        print("\n>>>>>>>>>>> Descending Arrangement of Element <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        ListOfFaveNum.sort()
        ListOfFaveNum.reverse()
        print("\nYou have Successfully Sorted the Elements in Descending arrangement.")
        print("\nThis is the New Descending Arrangement of Element:", ListOfFaveNum)
        print_menu()

    # (7) This is the Finding the Min Element Section:
    elif Choice == "7":
        print("\n>>>>>>>>>>> FIND THE MINIMUM ELEMENT <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        smallestnum = min(ListOfFaveNum)
        print("\nThe Smallest element is: ", smallestnum)
        print_menu()

    # (8) This is the Finding the Max Element Section:
    elif Choice == "8":
        print("\n>>>>>>>>>>> FIND THE MAXIMUM ELEMENT <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        largestnum = max(ListOfFaveNum)
        print("\nThe Largest element is: ", largestnum)
        print_menu()

    # (9) This is the Finding the Sum of all the Elements Section:
    elif Choice == "9":
        print("\n>>>>>>>>>>> FIND THE SUM OF ALL ELEMENTS <<<<<<<<<<<")
        print("Arrays", ListOfFaveNum)
        totalofelem= sum(ListOfFaveNum)
        print("\nThe SUM of all elements is: ", totalofelem)
        print_menu()

    # (10) Exit Program
    elif Choice == "10":
        print("\n>>>>>>>>>>> EXIT PROGRAM <<<<<<<<<<<")
        print(
            """\n
            >>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<
            -----------------------------------------------------
            ||     Thank you for using the Array Program!      ||
            ||                                                 ||
            ||                    Goodbye!                     ||
            ||                 Have a Nice Day                 ||
            ||=================================================||
            """
        )
        break

    # Unknown Choice of Menu
    else:
        print("Sorry but", Choice, "is not a valid option.")
        print_menu()
