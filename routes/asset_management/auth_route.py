from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
from models.asset_management.user_model import User
from schemas.asset_management.auth_schema import TokenData, AuthForm
from schemas.asset_management.user_schema import CreateUser
from jose import jwt
from passlib.context import CryptContext

secret = 'a very shady secret'
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def password_verify(plain, hashed):
    return pwd_context.verify(plain, hashed)

def password_hash(password):
    return pwd_context.hash(password)

router = APIRouter(
    prefix='/asset_management/api/Auth',
    tags=['Auth']
)

@router.post('/register')
def register(request: CreateUser, db: Session = Depends(get_db)):
    try:
        request.user_password = password_hash(request.user_password)
        if request.user_type == "" or request.user_type == "string":
            user = User(
            user_name = request.user_name,
            user_email = request.user_email,
            user_password = request.user_password,
            user_type = "Equipment Manager",
        )
        else:
            user = User(
                user_name = request.user_name,
                user_type = request.user_type,
                user_email = request.user_email,
                user_password = request.user_password
            )
        db.add(user)
        db.commit()
        return {'message': 'Registered Successfully!'}
    except Exception as e:
        print(e)

@router.post('/verify')
def verify(form: AuthForm, response: Response, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.user_email == form.user_email).first()
        if user:
            match = password_verify(form.user_password, user.user_password)
            if match:
                data = TokenData(user_name = user.user_name,
                                user_email = user.user_email,
                                user_id = user.user_id,
                                user_type = user.user_type)
                token = jwt.encode(dict(data), secret)
                response.set_cookie('token', token, httponly=True)
                return {'user':user, 'message': 'Log In Success!'}
        
        return {'message': 'User not found.'}
    except Exception as e:
        print(e)

@router.post('/logout')
def logout(response: Response):
    response.delete_cookie('token')
    response.delete_cookie('id')
    response.delete_cookie('email')
    response.delete_cookie('type')
    return {'message': 'Logout Success!'}