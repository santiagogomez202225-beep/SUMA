from django.http import HttpResponse
from django.shortcuts import render

# Función para la RESTA (Django)
def restar(request, a=None, b=None):
    if request.method == 'GET' and 'a' in request.GET and 'b' in request.GET:
        a = request.GET.get('a')
        b = request.GET.get('b')

    if a is not None and b is not None:
        try:
            resultado = float(a) - float(b)
            return HttpResponse(f"""
                <div style="font-family: Arial; text-align: center; margin-top: 50px;">
                    <h1 style="color: #2c3e50;">Resultado de la Resta 🚀</h1>
                    <h2 style="color: #27ae60;">La resta de {a} - {b} = {resultado}</h2>
                    <br><br>
                    <a href="/" style="padding: 12px 25px; background: #3498db; color: white; text-decoration: none; border-radius: 8px; font-weight: bold;">Volver a calcular</a>
                </div>
            """)
        except ValueError:
            return HttpResponse("Error: Asegúrate de ingresar números válidos.")
    
    return render(request, 'public/index.html')

# Función para la SUMA (Python puro)
def sumar(request, a=None, b=None):
    if request.method == 'GET' and 'a' in request.GET and 'b' in request.GET:
        a = request.GET.get('a')
        b = request.GET.get('b')

    if a is not None and b is not None:
        try:
            # Aquí hacemos la suma con Python nativo
            resultado = float(a) + float(b)
            return HttpResponse(f"""
                <div style="font-family: Arial; text-align: center; margin-top: 50px;">
                    <h1 style="color: #2c3e50;">Resultado de la Suma 🐍</h1>
                    <h2 style="color: #2980b9;">La suma de {a} + {b} = {resultado}</h2>
                    <br><br>
                    <a href="/" style="padding: 12px 25px; background: #3498db; color: white; text-decoration: none; border-radius: 8px; font-weight: bold;">Volver a calcular</a>
                </div>
            """)
        except ValueError:
            return HttpResponse("Error: Asegúrate de ingresar números válidos.")
            
    return render(request, 'public/index.html')