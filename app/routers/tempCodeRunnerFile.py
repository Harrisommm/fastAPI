from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/posts", tags=['Posts'])