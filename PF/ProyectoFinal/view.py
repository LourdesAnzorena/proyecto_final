
from django.http import HttpResponse
import datetime
#from django.template import Template, Context
#from django.template import loader
#plantilla= loader.get_template('index.html')
#documento=plantilla.render


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def diadehoy(request):
    dia=datetime.datetime.now()
    documentotextodia= f'Hoy es día:<br>{dia}'
    return HttpResponse(documentotextodia)


