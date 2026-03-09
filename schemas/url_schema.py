from pydantic import BaseModel

class Urlcreate(BaseModel):
    url : str

class Urlresponse(BaseModel):
    id : int
    url : str
    short_code : str

    class config:
        from_attributes = True