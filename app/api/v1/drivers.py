from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/drivers",
    tags=["Drivers"]
)


@router.get("/")
async def get_drivers():
    return {"message": "All drivers"}