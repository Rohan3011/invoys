from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from pdf.utils import render_to_pdf


class ViewPDF(View):
    def get(self, request):
        pdf = render_to_pdf("pdf/invoice.html")
        return HttpResponse(pdf, content_type="application/pdf")
