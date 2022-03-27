
from django.urls import path
from pdf.views import ViewPDF

urlpatterns = [
    path('pdf/', ViewPDF, name="view-pdf")
]
