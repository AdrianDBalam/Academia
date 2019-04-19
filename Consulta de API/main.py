import requests
if __name__ == '__main__':	
	class api:
		def consulta(self, codigo):
			url = 'https://restcountries.eu/rest/v2/alpha/'+codigo
			response = requests.get(url)
	
			if response.status_code == 200:
		
				response_json = response.json()
				nombre = response_json['name']
				bandera = response_json['flag']
				capital = response_json['capital']
				poblacion = response_json['population']
				print(nombre+'\n'+capital+'\n'+bandera)
				print(poblacion)

inicio = api()
pais = input("Ingrese el codigo del pais"+'\n')
inicio.consulta(pais)
