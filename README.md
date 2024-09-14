A micro-service for managing books in a library. Users can search through the catalogue of books and borrow them. There are two services in the application, the frontend service for enrolling users and other frontend related activities, and the admin/backend service for adding new books, deleting books and other admin related usage. 

It uses message brokers (celery and redis) to handle communication between the two services. When the admin adds a book to the catalogue the frontend api also gets updated with the latest book added by the admin.

### Usage
1. Clone the repo using `git clone https://github.com/ubterko/flask-library-app-api.git`
2. Install Redis and run `redis-server` (Linux)
2. Change directory to the individual folders
3. Using docker build the images using the instructions in the dockerfile for each api (admin_api, frontend_api)
   a. frontend api is exposed on port 5000
   b. admin api is exposed on port 5001 
4. Run the docker images 