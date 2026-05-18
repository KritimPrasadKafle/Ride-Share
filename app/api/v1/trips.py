from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/trips",
    tags=["Trips"]
)


@router.get("/")
async def get_trips():
    return {"message": "All trips"}