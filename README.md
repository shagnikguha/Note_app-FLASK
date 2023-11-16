Note_app-FLASK

This repository contains a simple notes app created using Flask and Jinja. The app allows users to:

    Create accounts
    Log in
    Create and delete multiple notes

Project Structure

    main.py: Entry point for the application. Run this file to start the website.

    website folder:

        auth.py: Manages user authentication and user-related functionalities.

        views.py: Contains the logic for each page of the website and controls their functionality.

        models.py: Defines and organizes the database. The database is managed and created using SQLAlchemy.

        __init__.py: Brings all the Python files together to set up the Flask application, which is later executed via main.py.

    static folder:
        index.js: JavaScript file responsible for allowing users to delete created notes.

    template folder:

        base.html: Acts as a template for other HTML files. Utilizes Jinja to interact with Flask.

        Other HTML files: Each file represents a page of the website and extends the base.html template.

How to Run

    Clone the repository:

    bash

git clone https://github.com/your-username/Note_app-FLASK.git

Install dependencies:

bash

pip install -r requirements.txt

Run the application:

bash

python main.py
