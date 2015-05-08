# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import time
import sys
import os


token = "Agui va el token de acceso"

lista = []

try:
	tag = sys.argv[1]
except:
	print "Hay que especificar un tag como parametro"
	sys.exit(0)

def download(url,id):
	try:
		img = urllib2.urlopen(url)
		f = file("imagen-%s.png"%id,'wb') 
		f.write(img.read())
		f.close()
	except:
		print 'No se puede descargar el archivo'


def listaImg(id):
	if id:
		url="https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s&count=5000&max_tag_id=%s" % (tag, token, id)
	else:
		url="https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s&count=5000" % (tag, token)

	page = urllib.urlopen(url).read()

	datos = json.loads(page)
	try:
		idNextPage = str(datos['pagination']['next_max_tag_id']).encode("utf-8")
		print idNextPage
		for x in datos['data']:
			lista.append(x['images']['standard_resolution']['url'])
			print x['images']['standard_resolution']['url']

		print "Esperamos 3 Seg."
		time.sleep(3)
		listaImg(idNextPage)

	except Exception, e:
		print str("Error:%s" % e)
		print len(lista)

listaImg(False)

continuar = raw_input("Se han encontrado %s imagenes, ¿Deseas descargarlas? (y / n): " % len(lista)) or "n"

if continuar == "y":
	try:
		fileName = tag+str(time.time())
		os.mkdir(fileName)
		os.chdir(fileName)
		for x in range(len(lista)):
			download(lista[x],x)
			print "imagen %s descargada" % x
			time.sleep(1)

	except Exception, e:
		print e

print "Proceso finalizado"
	
	



	


