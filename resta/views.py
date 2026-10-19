from django.http import HttpResponse
from django.shortcuts import render

def restar(request):
    # Intentamos obtener los números 'a' y 'b' de la URL (formulario)
    a = request.GET.get('a')
    b = request.GET.get('b')

    if a is not None and b is not None:
        try:
            resultado = float(a) - float(b)
            return HttpResponse(f"""
                <div style="font-family: Arial; text-align: center; margin-top: 50px;">
                    <h1 style="color: #2c3e50;">Resultado (Django) 🚀</h1>
                    <h2 style="color: #27ae60;">La resta de {a} - {b} = {resultado}</h2>
                    <br><br>
                    <a href="/" style="padding: 12px 25px; background: #3498db; color: white; text-decoration: none; border-radius: 8px; font-weight: bold;">Volver a calcular</a>
                </div>
            """)
        except ValueError:
            return HttpResponse("Error: Asegúrate de ingresar números válidos.")

    # Si no hay números (por ejemplo, entran a /restar/10/3/), mostramos la calculadora de nuevo.
    return render(request, 'index.html')