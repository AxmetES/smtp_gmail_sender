import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

import email_service
import schemas

router = APIRouter(prefix="/api", tags=["api"])
questions = []


@router.get("/home")
def read_root():
    return {"Hello": "World"}


@router.post("/send_email")
def send_email_endpoint(email: schemas.EmailSchema):
    try:
        email_service.send_email(email)
        return JSONResponse(content={"message": "Email sent"})
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=500, detail=str(e))