import logging
import uvicorn

from fastapi import FastAPI
from router import api


app = FastAPI()
app.include_router(api.router)


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("logs/logfile.log"), logging.StreamHandler()],
)

app.include_router(api.router)
logging.info(f'Email sender start')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
