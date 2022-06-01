from django.urls import path
from .views import todo_create_view,todo_list_view,todo_retrieveupdatedelete_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/',todo_list_view.as_view()),
    path('create/',todo_create_view.as_view()),
    path('rud/',todo_retrieveupdatedelete_view.as_view()),

]
