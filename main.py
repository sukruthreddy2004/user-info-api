from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "User Info API is running!"}

# User details route
@app.get("/user/{name}")
def get_user(name: str):
    return {
        "name": name,
        "message": f"Hello {name}, welcome to the API!"
    }
