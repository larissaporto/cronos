## API Documentation

### Início
- Este app foi feito com as seguintes tecnologias: python em sua versão 3.9.7, o framework django na versão 3.2.4 com o banco de dados Mysql.
- As requisições mínimas podem ser instaladas com o comando: `pip3 install -r requirements.txt`
- O API roda localmente na máquina no seguinte host: `http://localhost:8000/`
- Para alimentar o banco de dados rodar os seguintes comandos:
  `python manage.py loaddata teammember.json`
  `python manage.py loaddata service.json`
  `python manage.py loaddata post.json`
- Autenticação: Esta versão da aplicação só exige autenticação para a página do administrador `http://localhost:8000/admin/` e a sua criação pode ser feita utilizando o seguinte comando: `python3 manage.py createsuperuser`

### Endpoints 
#### GET /services/
#### GET /posts/
#### GET /teams/
- Geral:
    - Estes endpoints retornam uma lista de serviços/post/integrantes do time com seu um número total.
    - Esta lista é paginada em grupos de 10. A partir da 2 página tem que acrescentar o seguinte argumento na requisição `/services/?page=2`
- Example: `curl http://localhost:8000/services/`
```
{
    "count": 11,
    "next": null,
    "previous": "http://localhost:8000/services/",
    "results": [
        {
            "id": 5,
            "name": "Windows Sysadmin",
            "created": "2022-02-05T17:51:30.783236-03:00"
        }
    ]
}
```

#### GET /services/{id}/
#### GET /posts/{id}/
#### GET /teams/{id}/
- Geral:
    - Estes endpoints retornam um serviço/post/integrante de time específico de acordo com o seu id
- Example: `curl http://http://localhost:8000/teams/1/`
```
{
    "id": 1,
    "name": "John Wick",
    "job_title": "5"
}
```

#### DELETE /services/{id}/
#### DELETE /posts/{id}/
#### DELETE /teams/{id}/
- Geral:
    - Deleta um serviço/post/integrante de time específico de acordo com o seu id
- Example: `curl -X DELETE http://localhost:8000/services/1/`

#### POST /services/
#### POST /posts/
#### POST /teams/
- Geral:
    - Cria um serviço/post/integrante de time e retorna o objeto criado com os seguintes campos em cada endpoint 
    - serviços: name
    - posts: title, post
    - teams: name, job_title
        - job_title é uma categoria com escolhas determinadas aceitando somente escolhas de "1" a "5"
- Example: - `curl http://localhost:8000/teams/ -X POST -H "Content-Type: application/json" -d '{"name": "Skye", "job_title": "5"}'`
```
{
    "id":4,
    "name":"Skye",
    "job_title":"5"
}
```

#### PUT /services/{id}/
#### PUT /posts/{id}/
#### PUT /teams/{id}/
- Geral:
    - Atualiza por completo um serviço/post/integrante de time e retorna o objeto atualizado com os seguintes campos em cada endpoint 
    - serviços: name
    - posts: title, post
    - teams: name, job_title
        - job_title é uma categoria com escolhas determinadas aceitando somente escolhas de "1" a "5"
- Example: - `curl http://localhost:8000/teams/1/ -X PUT -H "Content-Type: application/json" -d '{"name": "John Wick", "job_title": "4"}'`
```
{
    "id":1,
    "name":"John Wick",
    "job_title":"4"
  }
```

#### PATCH /services/{id}/
#### PATCH /posts/{id}/
#### PATCH /teams/{id}/
- Geral:
    - Atualiza parcialmente um serviço/post/integrante de time e retorna o objeto atualizado os seguintes campos em cada endpoint 
    - serviços: name
    - posts: title, post
    - teams: name, job_title
        - job_title é uma categoria com escolhas determinadas aceitando somente escolhas de "1" a "5"
- Example: - `curl http://localhost:8000/teams/1/ -X PATCH -H "Content-Type: application/json" -d '{"job_title": "3"}'`
```
{
    "id":1,
    "name":"John Wick",
    "job_title":"3"
  }
```