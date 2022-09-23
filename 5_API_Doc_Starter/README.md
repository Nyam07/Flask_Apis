# API Documentation Practice
In this exercise, your task is to practice writing documentation for the bookstore app we created earlier.

You'll soon be writing documentation for your final project (the Trivia API), after which you'll get feedback from a reviewer. You can think of this as some rudimentary practice to prepare for that.

At each step, you can compare what you've written with our own version. Of course, **there isn't a single correct way to write a piece of documentation**, so your version may look quite different. However, there are principles and practices you should follow in order to produce quality documentation, and we'll point this out so you can check whether you've incorporated them in what you wrote.

## Getting started
Now, add a Getting Started section to your documentation. Remember, this should include at least your base URL and an explanation of authentication. Feel free to provide other information that is relevant for your API


## Error Handling
Now, add an Error Handling section to your documentation. It should include the format of the error responses the client can expect as well as which status codes you use.
- Response codes
- Messages
- Error types

## Endpoint Library
Now, add an Endpoint Library section to your documentation. Make sure that endpoints, methods and returned data are all clear. Consider including sample requests for clarity

- Organized by resource
- Include each endpoint
- Sample request 
- Arguments including data types
- Response object including status codes and data types 


# API REFERENCE

# Getting Started

- Base URL : At present the application can only be run locally on a the url http://127.0.0.1:5000/
- Authentication: This version of the application does not require any API Key authentication.

## Error Handling
Errors are returned as JSON objects in the following format:
{
    "success":False,
    "error": 400,
    "message":"bad request"
}

The api will return three trpes of errors when requests fail:
- 400: bad request
- 404: request not found
- 422: unprocessable

## Endpoints
#### GET/books
- General:
    - Returns a list of book values, success value and total number of books
    - Results are paginated in groups of 8. To change the page number, include a request argument starting from 1 in the request header.
- Sample:  curl http://127.0.0.1:5000/books

- Results:
    {
    "books": [
        {
        "author": "Stephen King", 
        "id": 1, 
        "rating": 5, 
        "title": "The Outsider: A Novel"
        }, 
        {
        "author": "Kristin Hannah", 
        "id": 3, 
        "rating": 4, 
        "title": "The Great Alone"
        }, 
        {
        "author": "Tara Westover", 
        "id": 4, 
        "rating": 5, 
        "title": "Educated: A Memoir"
        }, 
        {
        "author": "Jojo Moyes", 
        "id": 5, 
        "rating": 5, 
        "title": "Still Me: A Novel"
        }, 
        {
        "author": "Leila Slimani", 
        "id": 6, 
        "rating": 2, 
        "title": "Lullaby"
        }, 
        {
        "author": "Jordan B. Peterson", 
        "id": 11, 
        "rating": 5, 
        "title": "12 Rules for Life: An Antidote to Chaos"
        }, 
        {
        "author": "Kiese Laymon", 
        "id": 12, 
        "rating": 1, 
        "title": "Heavy: An American Memoir"
        }, 
        {
        "author": "Emily Giffin", 
        "id": 13, 
        "rating": 4, 
        "title": "All We Ever Wanted"
        }
    ], 
    "success": true, 
    "total_books": 13
    }

### POST/books
- Allows you to create a new book by submitting the title, author and rating. Returns the id of the created book, success value, the books in the current page and total number of books.
- Sample:  curl http://127.0.0.1:5000/books?page=2 -X POST -H "Content-Type: application/json" -d '{"title":"No going back", "author":"Benson Karani", "rating":"5"}'
- Results:
    {
    "books": [
        {
        "author": "Jose Andres",
        "id": 14,
        "rating": 4,
        "title": "We Fed an Island"
        },
        {
        "author": "Rachel Kushner",
        "id": 15,
        "rating": 1,
        "title": "The Mars Room"
        },
        {
        "author": "Gregory Blake Smith",
        "id": 16,
        "rating": 2,
        "title": "The Maze at Windermere"
        },
        {
        "author": "Neil Gaiman",
        "id": 23,
        "rating": 5,
        "title": "Neverwhere"
        },
        {
        "author": "Raila Odinga",
        "id": 24,
        "rating": 1,
        "title": "Justice"
        },
        {
        "author": "Neil Gaiman",
        "id": 25,
        "rating": 5,
        "title": "Neverwhere"
        },
        {
        "author": "Benson Karani",
        "id": 26,
        "rating": 5,
        "title": "No going back"
        }
    ],
    "created": 26,
    "success": true,
    "total_books": 15
    }

### POST/books/{search_term}
- Used to for books with titles that contain the search term provided. Returns succes value, books that match, and the total number of books that match.
- Sample:  curl http://127.0.0.1:5000/books -X POST -H "Content-Type: application/json" -d '{"search":"for"}'
- Results:
    {
    "books": [
        {
        "author": "Jordan B. Peterson",
        "id": 11,
        "rating": 5,
        "title": "12 Rules for Life: An Antidote to Chaos"
        }
    ],
    "success": true,
    "total_books": 1
    }

## PATCH/books/{book_id}
- This will update the ratings of the book with the selected book_id. It takes the book id and new rating as arguments. Returns success value and ID of the updated book.
- Sample: curl http://127.0.0.1:5000/books/25 -X PATCH -H "Content-Type:application/json" -d '{"rating":"4"}'
- Results: 
    {
        "id": 15,
        "success": true
    }

## DELETE/books/{book_id}
- This will delete the book with the specified book id. Returns success value, id of the book deleted, books in the current page and total number of books.
- Sample: curl http://127.0.0.1:5000/books/26 -X DELETE
- Results
    "books": [
        {
        "author": "Stephen King",
        "id": 1,
        "rating": 5,
        "title": "The Outsider: A Novel"
        },
        {
        "author": "Kristin Hannah",
        "id": 3,
        "rating": 4,
        "title": "The Great Alone"
        },
        {
        "author": "Tara Westover",
        "id": 4,
        "rating": 5,
        "title": "Educated: A Memoir"
        },
        {
        "author": "Jojo Moyes",
        "id": 5,
        "rating": 5,
        "title": "Still Me: A Novel"
        },
        {
        "author": "Leila Slimani",
        "id": 6,
        "rating": 2,
        "title": "Lullaby"
        },
        {
        "author": "Jordan B. Peterson",
        "id": 11,
        "rating": 5,
        "title": "12 Rules for Life: An Antidote to Chaos"
        },
        {
        "author": "Kiese Laymon",
        "id": 12,
        "rating": 1,
        "title": "Heavy: An American Memoir"
        },
        {
        "author": "Emily Giffin",
        "id": 13,
        "rating": 4,
        "title": "All We Ever Wanted"
        }
    ],
    "deleted": 26,
    "success": true,
    "total_books": 14
    }

