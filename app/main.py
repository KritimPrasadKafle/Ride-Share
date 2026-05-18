from fastapi import FastAPI
from app.api.v1.drivers import router as drivers_router
from app.api.v1.riders import router as riders_router
from app.api.v1.trips import router as trips_router

app = FastAPI(title="Ride Share API", version="1.0")

app.include_router(drivers_router)
app.include_router(riders_router)
app.include_router(trips_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Ride Share API!"}


@app.on_event("startup")
async def startup():
    from app.core.database import engine, create_tables
    await create_tables(engine)