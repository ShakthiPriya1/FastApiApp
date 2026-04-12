from fastapi import FastAPI, HTTPException, Request
from logger import logger

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "Hello World"}


@app.get("/greet")
def greet(name: str = "Guest"):
    logger.info(f"Greet called with name={name}")
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def add(a: int, b: int):
    result = a + b
    logger.info(f"Add called: {a} + {b} = {result}")
    return {"a": a, "b": b, "result": result}


@app.get("/error")
def simulate_error():
    logger.error("Simulated error triggered")
    raise HTTPException(status_code=400, detail="This is a simulated error")


@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        logger.error("Divide by zero attempted")
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = a / b
    logger.info(f"Divide called: {a} / {b} = {result}")
    return {"result": result}


@app.get("/crash")
def crash():
    logger.critical("Crash endpoint triggered")
    x = 10 / 0
    return {"result": x}