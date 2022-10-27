from django.shortcuts import render, redirect
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create your views here.
def index(request):
  if request.method == 'POST':
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(10, 73)
    textob.setFont("Helvetica", 14)

    lines = [
      request.POST['first_name'],
      request.POST['last_name'],
    ]

    for line in lines:
      textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="formulario.pdf")

  return render(request, 'index.html')

