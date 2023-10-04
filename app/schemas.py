from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    to: EmailStr
    subject: str
    message: str