from fastapi import FastAPI, Header, Response

app = FastAPI()

@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return {user_agent}

@app.post("/hi")
def greet(who: str = Header()):
    return {f"Hello? {who}?"}

@app.get("/hello")
def say_hello(status_code=200):
    return {":)"}

@app.get("/header/{name}/{value}")
def get_header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

@app.get("/happy")
def happy(status_code=200):
    return {":D"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True, host="localhost", port=8000)