# Basic HTTP Endpoint Project

This is a simple Python project that demonstrates how to create a basic HTTP endpoint using Python's built-in `http.server` module.

## Project Structure

The project has the following structure:
my_project/
├── server/
│ ├── init.py
│ └── endpoints.py
├── main.py
└── run_server.py


- `server/`: This directory contains the server code and endpoint logic.
- `__init__.py`: An empty file that makes the `server/` directory a Python package.
- `endpoints.py`: This file contains the logic for handling endpoints using `http.server`.
- `main.py`: This file is used to start the server and run the application.
- `run_server.py`: This script imports the server code and starts the HTTP server.

## How to Run the Project

1. Open a terminal or command prompt in the root directory of your project (`assignment-api`).

2. Run the following command to start the server:


3. The server will start running on `localhost` at port `8080`. You should see the following message in the terminal:


4. Now, you can access the endpoints in your browser or using tools like `curl` or `Postman`.

   - For the `/hello` endpoint: Open your web browser and go to `http://localhost:8080/ping`. You should see the response `Pong`.
   - For the `/about` endpoint: Open your web browser and go to `http://localhost:8080/passeord`. You should see the response that will give you random password 
   - For any other endpoint: If you visit any other URL, such as `http://localhost:8080/unknown`, you will see a `404 Not Found` response.

5. To stop the server, press `Ctrl + C` in the terminal where the server is running. This will gracefully shut down the server.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---