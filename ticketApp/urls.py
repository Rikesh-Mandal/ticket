from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.ticket_list),
<<<<<<< HEAD
    path('tickets/<int:ticket_id>', views.ticket_details),
    path('tickets/<int:ticket_id>/reply/', views.create_reply), #POST
    path('tickets/<int:ticket_id>/replies-by-ticket/', views.ticket_replies), #GET
    path('tickets/<int:ticket_id>/reply/<int:reply_id>/', views.update_delete_reply), #PUT and DELETE
=======
    path('tickets/<int:ticket_id>', views.ticket_details)
>>>>>>> new_branch
]