from fastapi import Body

from main import app
from profile_models import UserDent


@app.post('/api/register-user')
async def register_user(user_data: UserDent):
    print(user_data)

    return {'status': 1, 'message': 'Registration complete'}


@app.post('/api/login-user')
async def login_user(phome_number: int = Body(), password: str = Body()):
    checker = None

    return {'status': 1, 'message': 'Logged in'}




