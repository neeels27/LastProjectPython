import requests

Post = requests.post('http://127.0.0.1:5000/movies', json={'genre': 'Tragique', 'title': 'La haine', 'year': 1995}).status_code
if Post == 201:
    print(Post, "Bom")
else:
    print(Post, "Erro")     

Get = requests.get('http://127.0.0.1:5000/movies/1').status_code
if Get == 200:
    print(Get, "Bom")
else:
    print(Get, "Erro")  

Put = requests.put('http://127.0.0.1:5000/movies/3', json={'genre': 'Tragique', 'title': 'La haine', 'year': 2030}).status_code
if Put == 200:
    print(Put, "Bom")
else:
    print(Put, "Erro")  

Delete = requests.delete('http://127.0.0.1:5000/movies/1').status_code
if Delete == 200:
    print(Delete, "Bom")
else:
    print(Delete, "Erro") 