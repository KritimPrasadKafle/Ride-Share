from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/riders",
    tags=["Riders"]
)

@router.get("/")
def get_riders():
    return {"message": "All riders"}