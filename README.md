# Connect4 API

Python Flask  Connect4 API to evaluate board state

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python3 and pipenv to install Flask


```
pip install pipenv
```

### Installing

Start off by cloning this project to your local workspace

cd in project directoy and spawn a shell for pipenv to create a virtual environment in

```
cd Connect4-API
pipenv shell
```

Install Flask

```
pipenv install flask
```

Export FLASK_APP environment variable and run the server on port 8080

```
export FLASK_APP=api
flask run --port=8080
```

Now the server should be up and running on http://localhost:8080

## Testing Board State

Use your favorite API testing tool such as Postman or curl

### Example board state sent to server as application/json

```
{
    "board": [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 1, 0],
        [0, 0, 2, 2, 1, 1, 0],
        [0, 1, 1, 1, 1, 2, 0]
    ]       
}
```
You should receieve a HTTP Response 200 and message "Player 1 wins!"

### HTTP POST Endpoint for testing

```
http://localhost:8080/evaluate_board_state
```
