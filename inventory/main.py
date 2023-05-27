from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(host="redis-18670.c240.us-east-1-3.ec2.cloud.redislabs.com", port=18670,
            password="tWKfeTiveRIHvgE8ZX28N0g9sXgmf5uD", decode_responses=True)

class Product(HashModel):
    name:str
    price: float
    quantity: int

    class Meta:
        database: redis


@app.get("/products", )
async def root():
    return Product.all_pks()