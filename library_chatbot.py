
# College Library Chatbot

# Dictionary containing book titles and authors
books = {
    "python": "Python Programming by John Smith",
    "java": "Java Basics by James Gosling",
    "data structures": "Data Structures by Mark Weiss",
    "c programming": "C Programming by Dennis Ritchie",
    "computer networks": "Computer Networks by Andrew Tanenbaum"
}


# Function to display all books
def show_books():
    print("\nAvailable books in our library:")
    for title, author in books.items():
        print("-", author)


# Function to answer questions about books
def answer_question(question):
    question = question.lower()

    # Answer questions about available books
    if "book" in question and (
        "available" in question or "all" in question or "list" in question
    ):
        show_books()

    # Search for a book mentioned in the question
    else:
        found = False

        for title, details in books.items():
            if title in question:
                print("Yes! We have", details)
                found = True

        if not found:
            # Answer common library questions
            if "time" in question or "timing" in question or "open" in question:
                print("Our library is open Monday to Saturday, 9 AM to 5 PM.")

            elif "return" in question:
                print("Please return borrowed books on time.")

            elif "rule" in question or "rules" in question:
                print("Library rules: Maintain silence and handle books carefully.")

            elif "borrow" in question:
                print("Students can borrow books from the library. Please check with the librarian for borrowing limits.")

            elif "hello" in question or "hi" in question:
                print("Hello! How can I help you with library books?")

            else:
                print("Sorry, I couldn't understand your question.")
                print("Try asking about available books, Python, Java, timings, or library rules.")


# Main chatbot function
def library_chatbot():
    print("===================================")
    print("   COLLEGE LIBRARY CHATBOT")
    print("===================================")

    name = input("Hello! What is your name? ")
    print("\nHi", name + "!")
    print("Ask me questions about library books.")
    print("Type 'books' to view all books.")
    print("Type 'exit' to end the conversation.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Chatbot: Thank you for visiting the library. Goodbye!")
            break

        elif question.lower() == "books":
            show_books()

        elif question == "":
            print("Chatbot: Please enter a question.")

        else:
            print("Chatbot:", end=" ")
            answer_question(question)


# Start the chatbot
library_chatbot()
