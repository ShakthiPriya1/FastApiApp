from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Shakthi!!"}


@app.get("/greet")
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def add(a: int, b: int):
    return {"a": a, "b": b, "result": a + b}

@app.get("/error")
def simulate_error():
    raise HTTPException(status_code=400, detail="This is a simulated error")


@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}