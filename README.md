# Note App with Flask

This repository contains a simple notes app created using Flask, Jinja, HTML, and SQLAlchemy. It enables users to manage their notes with ease.
## Features

- User registration and login
- Create and delete multiple notes
- Store notes securely in a database

## Project Structure

- **main.py:** The entry point for the application. Run this file to start the website.

- **website folder:**
    - auth.py: Manages user authentication and user-related functionalities.
    - views.py: Contains the logic for each page of the website and controls their functionality.
    - models.py: Defines and organizes the database. The database is managed and created using SQLAlchemy.
    - __init__.py: Brings all the Python files together to set up the Flask application, which is later executed via main.py.

- **website/static folder:**
     - index.js: JavaScript file responsible for allowing users to delete created notes.

- **website/templates folder:**
     - base.html: Acts as a template for other HTML files. Utilizes Jinja to interact with Flask.
     - Other HTML files: Each file represents a page of the website and extends the base.html template.

## Installation and Usage

  ####  Clone the repository:

        git clone https://github.com/your-username/Note_app-FLASK.git

  ###   Running the code:
  
        python3 main.py

  Ensure that you are in the proper working directory when running these commands.
