from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_data():
    return {"test" : "welcome to test"}



if _name_ == "_main_":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)