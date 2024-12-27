# Library Management System API

This project implements a basic **Library Management System** API using **Flask**. The system supports **CRUD operations** for managing books and members, **token-based authentication**, **search functionality** for books, and **pagination** for book listings.

## Table of Contents

- [How to Run the Project](#how-to-run-the-project)
- [Design Choices Made](#design-choices-made)
- [Assumptions and Limitations](#assumptions-and-limitations)

---

## How to Run the Project

Follow these steps to set up and run the **Library Management System API** on your local machine.

### 1. Prerequisites

Ensure you have the following installed on your machine:

- **Python** (Version 3.6 or higher)
- **pip** (Python's package installer)

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

`python -m venv venv`
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`
**Install the required dependencies:**
  `pip install Flask`

### 3. Run the Application
Once the dependencies are installed, you can start the Flask server by running the app.py file:
 `python -m venv venv`

The application will start running on `http://127.0.0.1:5000/`. You can now make API requests to this endpoint using tools like Postman or cURL.

### 4. Testing the API
  Once the server is running, you can test the different API routes as follows:

  -`Login (to get a token): POST /login`
  -`Request body: { "email": "member@example.com" }`
  -`Response: { "token": "generated-token" }`
  -`Add Book: POST /books`

  Headers: Authorization: <generated-token>
  Request body:
  **Search Books:** `GET /books/search?title=Flask`
  **Query parameters:** `title=Flask`
  Response: Books matching the search query.

### 5. Example Requests
-**Get a list of books:** `GET /books?page=1`
-**Get details of a single book:** `GET /books/{id}`
-**Update a book:** `PUT /books/{id}`
-**Delete a book:** `DELETE /books/{id}`

## Design Choices Made
  ### 1. Flask Framework:
  Flask is a micro web framework that is lightweight, easy to use, and ideal for building small APIs. It is used in this project due to its simplicity and flexibility.
  ### 2. In-Memory Data Storage:
   For simplicity, book and member data is stored in memory (using Python lists). This makes the app quick to set up but limits scalability and persistence.
  ### 3. Token-Based Authentication:
  A simple token-based authentication system is used to ensure that only authorized users can perform sensitive actions like adding, updating, or deleting books.
### 4. Pagination:
  Pagination has been implemented for listing books. By default, each request returns 5 books per page, but this can be adjusted to handle larger datasets.
### 5. Book Search:
  The search functionality supports searching books by title and author. The search is case-insensitive and returns matching books.
### 6. Flask Routing:
  Each route is dedicated to a specific task such as adding, updating, or deleting books. This ensures clear, simple, and readable code.

## Assumptions:
  **In-Memory Data:** The system assumes that the book and member data are stored in-memory, meaning it will be lost if the server restarts. For a production system, a database should be used.

  **Token Authentication:** The system assumes users log in with a valid email address, generating a unique token for authentication in subsequent requests.

  **No External Dependencies:** The system uses Flask only, with no additional complex dependencies or libraries.

## Limitations:
  **Limited Data Persistence:** The data (books and members) is lost when the application restarts. For production, using a database like SQLite or PostgreSQL is recommended.

  **Basic Error Handling:** Error handling is minimal, and only basic error messages are provided. More robust error reporting could be added.

  **Security:** The token authentication doesn't include password hashing, which is essential for security in real applications.

  **No Pagination for Search:** The search feature does not include pagination, which could be necessary for large numbers of search results.

  **No Rate Limiting:** There is no rate limiting in place, making the API susceptible to excessive requests in case of high traffic.

  **No Frontend:** This is an API-only solution. A frontend interface would need to be built separately for interacting with the API.  
  
