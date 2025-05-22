from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(exam, diagnosis, status_df):
    buffer = BytesIO()  # cria buffer em memória
    c = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica", 14)
    c.drawString(50, altura - 50, "Blood test result")

    c.setFont("Helvetica", 10)
    y = altura - 100
    for coluna, valor in exam.iloc[0].items():
        c.drawString(50, y, f"{coluna}: {str(valor)}")
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Diagnosis: {str(diagnosis[0])}")
    
    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Prediction details:")
    
    c.setFont("Helvetica", 10)
    y -= 20
    for coluna, valor in status_df.iloc[0].items():
        c.drawString(50, y, f"{coluna}: {str(valor)}")
        y -= 15
        if y < 50:
            c.showPage()
            y = altura - 50

    c.save()
    buffer.seek(0)  # volta o ponteiro para o início
    return buffer.getvalue()  # retorna os bytes do PDF

