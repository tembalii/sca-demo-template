from fastapi import FastAPI
from sqlalchemy.orm import relationship

app = FastAPI()

@app.get("/direct/{input}")
def direct_response(input: str):

    from .models import Child
    from .models import Parent

    tainted = input

    # ruleid: sqlalchemy-fastapi-relationship
    Parent.children = relationship(Child, primaryjoin=f"Parent.id == {tainted}")

    # ruleid: sqlalchemy-fastapi-relationship
    Parent.children = relationship(Child, foreign_keys=f"Parent.id == {tainted}")
