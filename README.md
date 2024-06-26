# EMBRAPA - Dados da Vitivinicultura
## This is a simple API for a FIAP - Tech Challenge (Pós-tech Machine Learning Engineering)
Currently hosted on Google Cloud Run (built & deployed on repo push) at: https://embrapa-vitivinicultura-api-atuc6xwo4q-rj.a.run.app/ui/


"Estamos apresentado informações referentes à quantidade de uvas processadas, produção e comercialização de vinhos, suco e derivados provenientes do Estado do Rio Grande do Sul, que representa mais de 90% da produção nacional. Apresentamos também os dados de importações e exportações dos produtos da vitivinicultura.

Alguns esclarecimentos se fazem necessários, para que os usuários façam o uso correto das informações:

Os vinhos nacionais são classificados para fins estatísticos em vinho de mesa (elaborados com uvas americanas e/ou híbridas), vinho fino de mesa (elaborados com uvas Vitis Vinifera L.) e vinho especial (corte de vinho de mesa e fino de mesa).
Os vinhos importados, denominados de vinhos de mesa são equivalentes aos vinhos finos de mesa nacionais, pois são elaborados com uvas Vitis Vinifera L.
Os dados constantes da base de dados ALICEweb, referentes à vinhos e espumantes são expressos em quilos, no entanto considerando que a densidade desses produtos é de aproximadamente um (1), consideramos 1 Kg = 1L.
Os arquivos de download possuem a extensão CSV, para facilitar a importação em planilhas ou banco de dados."

Source: http://vitibrasil.cnpuv.embrapa.br/index.php


## Requirements
Python 3.10+

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
