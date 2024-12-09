'''

Experiment No. 3 :
            Write a Python program to store marks scored in subject “Fundamental of Data Structure”. Write 
            functions to compute following: Write a Python program for department library which has N 
            books, write functions for following:

            1) Delete the duplicate entries
            2) Display books in ascending order based on cost of books
            3) Count number of books with cost more than 500.
            4) Copy books in a new list which has cost less than 500.

'''

n = int(input("Enter the number of books: "))
books = []

for book in range(n):
    # name = input(f"Enter the name of book {book + 1}: ")
    name = input("Enter the name of book : ")
    price = float(input(f"Enter the price of book {name}: "))  # Assuming prices are entered as floats
    books.append((name, price))

print("List of books with their prices:")
for book in books:
    print(f"{book[0]}: {book[1]}")


# Ascending order of prices
def inc_price():
    books.sort(key=lambda x: x[1])
    print("Books in ascending order of price:")
    for book in books:
        print(f"{book[0]}: {book[1]}")


# Books with prices more than 500
def more_tn_500():
    moreThan500 = [book for book in books if book[1] > 500]
    print("Books with price more than 500 Rupees:")
    for book in moreThan500:
        print(f"{book[0]}: {book[1]}")


# Books with prices less than or equal to 500
def less_tn_500():
    lessThan500 = [book for book in books if book[1] <= 500]
    print("Books with price less than or equal to 500 Rupees:")
    for book in lessThan500:
        print(f"{book[0]}: {book[1]}")


# Detect duplicates in prices
def delete_duplicates():
    unique_books = []
    prices_seen = []

# Loop through each book and check if the price has been seen before
    for book in books:
        price = book[1]
        if price not in prices_seen:
            unique_books.append(book)
            prices_seen.append(price)

    # Print books with no duplicate prices
    print("Books with no duplicate prices:")
    for book in unique_books:
        print(f"{book[0]}: {book[1]}")

    print(unique_books)



def duplicate():
    prices = [book[1] for book in books]
    no_dupes = list(set(prices))

    print("Books with no duplicate prices:")
    for price in no_dupes:
        for book in books:
            if book[1] == price:
                print(f"{book[0]}: {book[1]}")

    dupes = [price for price in prices if prices.count(price) > 1]
    print("Books with duplicate prices:")
    for price in dupes:
        for book in books:
            if book[1] == price:
                print(f"{book[0]}: {book[1]}")


# Execute functions here
flag = 1
while flag == 1 :
    
    print("""choose number from (1 to 5) to perform the function. 
1) Delete the duplicate entries
2) Display books in ascending order based on cost of books
3) Count number of books with cost more than 500.
4) Copy books in a new list which has cost less than 500.
5) To End program.
        """)
    
    ch = int(input("Enter choise : "))

    if ch == 1 :
        delete_duplicates()
        remind = input("Choose Yes/No for further data.")
        if remind == 'Yes' :
            flag = 1
        if remind == 'No' :
            print("Thank You")
            flag = 0
    
    elif ch == 2 :
        inc_price()
        remind = input("Choose Yes/No for further data.")
        if remind == 'Yes' :
            flag = 1
        if remind == 'No' :
            print("Thank You")
            flag = 0
    
    elif ch == 3 :    
        more_tn_500()
        remind = input("Choose Yes/No for further data.")
        if remind == 'Yes' :
            flag = 1
        if remind == 'No' :
            print("Thank You")
            flag = 0
    
    elif ch == 4 :
        less_tn_500()
        remind = input("Choose Yes/No for further data.")
        if remind == 'Yes' :
            flag = 1
        if remind == 'No' :
            print("Thank You")
            flag = 0
    
    elif ch == 5 :
        print("Thank You")
        break

# <---------------- NICE ONE :) ----------------->
