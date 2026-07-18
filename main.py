from fastapi import FastAPI

app = FastAPI()


def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return None
    return a + b


@app.get("/")
def read_root():
    return {"message": "Hello from ci_cd_learn"}


@app.get("/add")
def add_endpoint(a: int, b: int):
    return {"result": add(a, b)}
