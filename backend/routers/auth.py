from fastapi import APIRouter

router = APIRouter(prefix="/api/user", tags=["Auth"])

@router.get("/me")
def get_current_user():
    return {"name": "Assimilate Developer"}

