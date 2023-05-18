from django.conf import settings
from django.urls import path,include
from theme_pixel import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import reverse


urlpatterns = [
  
    path("admin/", admin.site.urls),
    # Pages
    path('home/templates/pages/formulaireBi/', views.FormulaireBI, name="FormulaireBI"),
    
    path('', views.index,name='index'),
    path('about-us/', views.abouts_us, name='about_us'),
    path('datatable/<int:id>', views.datatable , name='datatable'),
    path('excel-to-image/<int:id>/', views.excel_to_image, name='excel_to_image'),

    
   
    path('rate/<int:id>/<int:rating>/', views.rate),
    path('contact-us/', TemplateView.as_view(template_name='pages/contact-us.html'), name='contact_us'),
    path('landing-freelancer/', views.landing_freelancer, name='landing_freelancer'),
    path('Details_plan/<int:id>', views.Details, name='details_plan'),
    path('blank/', views.blank_page, name='blank'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/templates/pages/Study-Plan/home/templates/pages/dashboard.html/', views.dashboard, name='dashboard'),
    path('csv/<int:id>', views.csv_view, name='csv'),
    path('add-product/', views.addProduct, name="add-prod"), 
    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
        path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
