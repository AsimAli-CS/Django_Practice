from django.urls import path , include
from . import views

app_name = 'user'

urlpatterns = [
    path('show/', views.show_email, name="show" ),
    path('detail/<int:id>', views.detail, name="detail1" ),
    path('email/',views.email_temp,name="email_temp"),
    path('show_email_cbv/',views.Show_Email.as_view(), name = "show_cbv"),
    path('Detail/<int:id>',views.Detail.as_view(), name = "DetailView"),
    path('user/',views.user_view, name = "user"),
    path('update/<int:id>', views.update_user, name='update_user'),
    
]
