import requests
from fastapi import APIRouter

router = APIRouter()


@router.get("/clients")
def get_products():
    with requests.Session() as sess:
        response = sess.get('https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223'
                            '-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes')
        return response.json()
