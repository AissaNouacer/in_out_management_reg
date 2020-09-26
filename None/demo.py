#import io
from reportlab.pdfgen import canvas


#def some_gen(request):
    # Create a file-like object buffer to recive pdf data.
#    buffer = io.BytesIO()
    #Create pdf object
p = canvas.Canvas('hello.pdf')

# Draw things on the pdf.
p.drawString(0,8,"Hello World! ")
p.drawString(40,25,"Hello Second! ")
p.drawString(100,50,"Hello THeered! ")


    # close the pdf object cleanly.

#p.showPage()
p.save()



