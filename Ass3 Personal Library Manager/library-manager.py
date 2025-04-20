import json
from json.tool import main
import os

data_file = 'library.json'


def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
        return[]
    
    def save_library(library):
        with open(data_file, 'w') as file:
            json.dump(library, file)
                
    
    def add_book(library):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the year of the book: ")
        genre = input("Enter the genre of the book: ") 
        read = input("Have you read this book? (yes/no): ").lower() == 'yes'
        new_book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read
        }
        library.append(new_book)
        save_library(library)
        print(f"Book '{title}' added successfully.")
        
        
    def remove_book(library):
        title = input("Enter the title book to remove from library: ")
        initial_length = len(library)
        library = [book for book in library if book['title'].lower() != title.lower()]
        if len(library) < initial_length:
            save_library(library)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found in the library.")
            
            
    def search_library(library):
        search_by = input("Search by (title/author/year/genre): ").lower()
        search_value = input(f"Enter the {search_by}: ").lower()
        
        results = [book for book in library if search_value in book[search_by].lower()]
        
        if results:
            for book in results:
                status = "Read" if book['read'] else "Not Read"
                print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        else:
            print("Library is empty.")
            
            
    def display_all_books(library):
        if library:
            for book in library:
                status = "Read" if book['read'] else "Not Read"
                print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        else:
            print("Library is empty.")
            
    def display_statistics(library):
        total_books = len(library)
        read_books = len([book for book in library if book['read']])
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.2f}%")
         
         
    def main():
        library = load_library()
        while True:
            print("Menu:")
            print("1. Add a Book")
            print("2. Remove a Book")
            print("3. Search the Library")
            print("4. Display all books")
            print("5. Display Statistics")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                add_book(library)
            elif choice == '2':
                remove_book(library)
            elif choice == '3':
                search_library(library)
            elif choice == '4':
                display_all_books(library)
            elif choice == '5':
                display_statistics(library)
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
              
              
if __name__ == "__main__":
    main()        
        
        
        
        