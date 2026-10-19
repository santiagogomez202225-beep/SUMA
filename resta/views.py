from django.http import HttpResponse

def restar(request, a, b):
    try:
        resultado = float(a) - float(b)
        # Un pequeño diseño para que se vea bien en el navegador
        html = f"""
        <div style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Resultado de la Resta (Django) 🚀</h2>
            <h1 style="color: #2c3e50;">La resta de {a} - {b} = {resultado}</h1>
            <br>
            <a href="/" style="padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px;">Volver al inicio</a>
        </div>
        """
        return HttpResponse(html)
    except ValueError:
        return HttpResponse("Error: Asegúrate de ingresar números válidos en la URL.")