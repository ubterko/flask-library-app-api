A micro-service for managing books in a library. Users can search through the catalogue of books and borrow them. There are two services in the application, the frontend service for enrolling users and other frontend related activities, and the admin/backend service for adding new books, deleting books and other admin related usage. 

It uses message brokers (celery and redis) to handle communication between the two services. When the admin adds a book to the catalogue the frontend api also gets updated with the latest book added by the admin.

### Usage
1. Clone the repo using `git clone https://github.com/ubterko/flask-library-app-api.git`
2. Install the requirement `pip install -r requirements.txt`
3. Set your environment variables
   a. `set SECRET_KEY=your_secret_key`
   b. `set FLASK_APP=admin_api --port=5001`
   c. `flask run`
   c. start different server `set FLASK_APP=frontend_api --port=5002` & `flask run`
