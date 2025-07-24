

##  Major Issues Identified in Original Code

1. Entire code has a single file structure  (`app.py`) with all routing, logic, DB code, and responses mixed together
2. There is SQL injection vulnerability due to use of raw query strings
3. Plain-text password storage - passwords are stored as strings without any hashing or encryption
4. No input validation — blindly accessed keys from request data
5. No error handling — potential for crashes or server 500s
6. Repetition of logic —  `try-except` and validation done manually in multiple places
7. Lack of proper HTTP status codes — all responses returned plain text with 200 OK
8. No test coverage — no confidence in correctness or regressions

---

##  Key Changes Made

###  Code Organization
- Restructured into MVC-style layout:to follow best practices of rest api design
  - `controllers/` — business logic
  - `models/` — database interaction
  - `views/` — response formatting(the content visible to client user)
  - `routes/` — endpoint registrations
  - `utils/` — helper functions (e.g., JSON parsing),decorators
  

###  Security Improvements
- Used parameterized queries to prevent SQL injection
- Replaced plain-text password storage with bcrypt-style hashing via `werkzeug.security`
- Added input validation using `parse_json_request()`

###  Error Handling
- Wrapped all controller logic in a reusable `@handle_exceptions` decorator
- Added a global Flask error handler (`@app.errorhandler(Exception)`)
- Views consistently return meaningful HTTP status codes (400, 401, 404, 500)

###  Code Reusability
- Moved reusable logic (e.g., request parsing, error formatting) into `utils.py` and `views.py`
- Replaced repeated `try-except` logic with decorator

###  Testing
- Created `tests/` folder with:
  - `conftest.py`: Flask test client fixture
  - `test_routes.py`: Tests for `/`, `/users`, `/login`, `/search` endpoints
- Ensures critical functionality is covered

---

##  Assumptions 

- Assumed the schema for `users` table (id, name, email, password) would remain unchanged
- Continued using SQLite for simplicity; did not introduce an ORM (e.g., SQLAlchemy) to keep code close to the original
- Assumed minimal frontend or external API consumers (no CORS, auth tokens, pagination, etc.)
- Did not implement detailed validation schema (e.g., regex, email format) to stay within scope

---

## If I Had More Time

- Add unit tests for `models/`, `controllers/`, and `utils/`
- Use Pydantic or Marshmallow for robust input validation
- Add JWT-based authentication instead of just login checks
- Implement rate limiting and account lockout for brute-force protection
- Use SQLAlchemy ORM for better DB abstraction and flexibility
- Add logging to capture all warnings and exceptions
- Configure separate environments (dev, test, prod) with `.env` variables

---

##  AI Tools Used
- ChatGPT (for  testing setup, and summarizing the changes done and creating the readme file)
- All AI-generated code was reviewed and manually integrated/validated
