from django.http import HttpResponse

def restar(request, a, b):
    resultado = float(a) - float(b)
    return HttpResponse(f"La resta de {a} - {b} = {resultado}")