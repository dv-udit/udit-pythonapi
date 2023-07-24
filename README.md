# Assignment API

This is a Python project that demonstrates how to create a basic HTTP server with custom endpoints and a password generator using the `pkgUdit` package.

## Getting Started

To run the project, follow these steps:

1. Install the required packages:

```bash
pip install -r requirements.txt
```
2. Start the server:
``` 
python run_server.py
```
3. Access the endpoints:

* To ping the server, go to `http://localhost:8080/ping`

* To generate a password, go to `http://localhost:8080/password`

4. Project Structure
The project has the following structure:
* server/: This directory contains the server code and endpoint logic.
*  `__init__.py`: An empty file that makes the server/ directory a Python package.
* endpoints.py: This file contains the logic for handling endpoints using http.server.
* main.py: This file is used to start the server and run the application.
* run_server.py: This script imports the server code and starts the HTTP server.

# How to Run the Project

* Open a terminal or command prompt in the root directory of your project (udit-pythonapi).

* Run the following command to start the server:
```
python run_server.py
```
* The server will start running on localhost at port 8080. You should see the following message in the terminal:
```
Server is running on http://localhost:8080
```
4. Now, you can access the endpoints in your browser or using tools like curl or Postman.

* For the /ping endpoint: Open your web browser and go to `http://localhost:8080/ping` You should see the response `Pong!`.
* For the /password endpoint: Open your web browser and go to `http://localhost:8080/password`. You should see the response with the generated password.

```
Note: The password will vary each time you access the /password URL since it is generated dynamically using the generate_pass() function from the pkgUdit package.
```
To stop the server, press Ctrl + C in the terminal where the server is running. This will gracefully shut down the server.

# Requirements
Python (version >=3)

pkgUdit (version 1.1.5.5)