from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="School Admission Assistant",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():

    return {
        "message":"School Admission Assistant API Running"
    }