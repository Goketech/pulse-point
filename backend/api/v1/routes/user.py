from typing import Annotated, Optional, Literal
from fastapi import Depends, APIRouter, Request, status, Query, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api.utils.success_response import success_response
from api.v1.models.user import User
from api.v1.schemas.user import (
    AllUsersResponse, UserUpdate
)
from api.db.database import get_db
from api.v1.services.user import user_service


user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get('/delete', status_code=200)
async def delete_account(request: Request, db: Session = Depends(get_db), current_user: User = Depends(user_service.get_current_user)):
    '''Endpoint to delete a user account'''

    # Delete current user
    user_service.delete(db=db)

    return success_response(
        status_code=200,
        message='User deleted successfully',
    )

@user_router.patch("",status_code=status.HTTP_200_OK)
def update_current_user(
    current_user : Annotated[User , Depends(user_service.get_current_user)],
    schema : UserUpdate,
    db : Session = Depends(get_db),
):

    user = user_service.update(db=db, schema= schema, current_user=current_user)

    return success_response(
        status_code=status.HTTP_200_OK,
        message='User Updated Successfully',
        data= jsonable_encoder(
            user,
            exclude=['password', 'is_deleted', 'is_verified', 'updated_at', 'created_at', 'is_active']
        )
    )


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(
    user_id : str,
    db : Session = Depends(get_db),
    current_user: User = Depends(user_service.get_current_user)
):
    
    user = user_service.get_user_by_id(db=db, id=user_id)

    return success_response(
        status_code=status.HTTP_200_OK,
        message='User retrieved successfully',
        data = jsonable_encoder(
            user, 
            exclude=['password', 'is_deleted', 'is_verified', 'updated_at', 'created_at', 'is_active']
        )
    )