from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/")
def greet(who: str):
    return {f"Hello? {who}?"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True, host="localhost", port=8000)