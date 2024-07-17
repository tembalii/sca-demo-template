from rest_framework.decorators import api_view
from sqlalchemy.orm import relationship


@api_view(["GET", "POST"])
def snippet_list(request):
    tainted = request.GET["query"]

    from .models import Child
    from .models import Parent

    # ruleid: sqlalchemy-django-relationship
    Parent.children = relationship(Child, primaryjoin=f"Parent.id == {tainted}")

    # ruleid: sqlalchemy-django-relationship
    Parent.children = relationship(Child, foreign_keys=f"Parent.id == {tainted}")
