import requests
from bs4 import BeautifulSoup
from googlesearch import search
from os import system
#conocer precio del dolar blue venta para futuras conversiones
#dolar = precioDolar()

#conocer precio de venta de un juego en steam
def menu():
	opcion = "1"
	print("\n1 - Ingresar otro juego \n2- Salir")
	opcion = input()
	if opcion == "1":
		system("cls")
		main()
	elif opcion == "2":
		system("exit")
	else:
		system("cls")
		print("Opcion no valida")
		menu()

def main():
	juego = input("ingrese nombre del juego a conocer precio: ")
	juego = juego + " steam"
	tld = "com"
	lang ="es"
	num= 1
	start=0
	stop=num
	pause=2.0
	
	try:
		result = search(juego, tld=tld, lang=lang, num=num, start=start, stop=stop, pause=pause)
	except:
		print("Juego no encontrado")
		menu()
	for i in result:
		urlJuego = i
	
	try:
		htmlJuego = requests.get(urlJuego)
	except:
		print("Juego no encontrado")
		menu()
	soup = BeautifulSoup(htmlJuego.content, 'lxml')
	try:
		nombreJuego = soup.find('div', class_="apphub_AppName").text
	except:
		print("Juego no encontrado")
		menu()
	try:
		precioJuego = soup.find('div', class_="game_purchase_price price").text
	except:
		precioJuego = soup.find('div', class_="discount_final_price").text
	precioJuego = precioJuego.strip()
	precioJuego = precioJuego.replace(" ", "")
	
	if precioJuego == "Free to Play" or precioJuego == "Free to Play ":
		print(f"{nombreJuego} es gratis en Steam")
	else:
		print(f"{nombreJuego} cuesta {precioJuego} en Steam")
	menu()

main()