#!/usr/bin/python3
""" user class """

from models.base_model import BaseModel


class User(BaseModel):
    """class user with details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
