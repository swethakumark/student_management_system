from django.urls import path
from . import views

urlpatterns = [
    path('show/',views.Shows.as_view(),name='show'),
    path('edit/',views.Edit.as_view(),name='edit'),
    path('form',views.Form.as_view(),name='form'),
    path('delete/',views.Delete.as_view(),name='delete'),

    path('editprofile/',views.Editprofile.as_view(),name='editprofile'),
    path('loginhome/',views.Home.as_view(),name='loginhome'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('staff/',views.Staffs.as_view(),name='staff'), 
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),

]
