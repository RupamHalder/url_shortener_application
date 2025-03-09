# URL Shortener

## Overview
This is a Django-based URL Shortener application that allows users to shorten long URLs into compact, shareable links.

## Features
- Shorten long URLs into compact links.
- User-friendly interface for generating and managing URLs.
- Automatic redirection to the original URL when a shortened link is visited.
- Django-based backend for handling URL storage and redirection.

## Technologies Used
- **Backend:** Django (Python)
- **Database:** SQLite (default) or PostgreSQL/MySQL (optional)
- **Frontend:** HTML, CSS, JavaScript

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Steps to Set Up the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RupamHalder/url_shortener_application.git
   cd url_shortener_application
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Configuration Files**
* Create .env file in main project directory and add your database credentials as follows.

   ```bash
    DB_NAME="<Database name>"
    DB_USER="<Database username>"
    DB_PASSWORD="<Database password>"
    DB_HOST="<Database host name>"
    DB_PORT="<Database port>"
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   The application will be available at `http://127.0.0.1:8000/`.

## Usage
1. Navigate to the homepage.
2. Enter a long URL in the provided input field.
3. Click the "Shorten URL" button.
4. Go to list by clicking on "Home" button in navigation bar.
4. Copy the generated short URL and share it.
5. Visit the short URL to be redirected to the original link.

---
Feel free to contribute and improve this project!

