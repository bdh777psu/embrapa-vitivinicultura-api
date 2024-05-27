import os
import connexion
import six
import pandas as pd
import requests

from swagger_server.models.comercializacao_item import ComercializacaoItem  # noqa: E501
from swagger_server.models.exportacao_item import ExportacaoItem  # noqa: E501
from swagger_server.models.importacao_item import ImportacaoItem  # noqa: E501
from swagger_server.models.processamento_item import ProcessamentoItem  # noqa: E501
from swagger_server.models.producao_item import ProducaoItem  # noqa: E501
from swagger_server import util


def download_csv(url):
    file_name = url.split('/')[-1]
    save_path = os.path.join("data/", file_name)

    if os.path.exists(save_path):
        print(f"File already present at: {save_path}")
    else:
        response = requests.get(url)

        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
        else:
            print("Error: " + str(response.status_code))

    return save_path


def search_comercializacao(produto, ano=None):  # noqa: E501
    """searches Comercializacao

    By passing in the appropriate options, you can search for available Comercializacao info in the system  # noqa: E501

    :param produto: search for a product name
    :type produto: str
    :param ano: search for a specific year
    :type ano: str

    :rtype: List[ComercializacaoItem]
    """

    result = []

    file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv")
    data = pd.read_csv(file, sep=';')
        
    all_product_info = data[data['Produto'] == produto]

    if ano is None:
        for index, year in enumerate(all_product_info):
            if index >= 3:
                product = all_product_info['Produto'].values[0]
                quantity = all_product_info[year].values[0]

                item = ComercializacaoItem(categoria=product,
                                        cultivar=produto,
                                        ano=int(year),
                                        quantidade=int(quantity)
                                        ).to_dict()

                result.append(item)
    else:
        product = all_product_info['Produto'].values[0]
        quantity = all_product_info[ano].values[0]
                
        item = ComercializacaoItem(categoria=product,
                                        cultivar=produto,
                                        ano=int(ano),
                                        quantidade=int(quantity)
                                        ).to_dict()

        result.append(item)
    return result


def search_exportacao(categoria, pais, ano=None):  # noqa: E501
    """searches Exportacao

    By passing in the appropriate options, you can search for available Exportacao info in the system  # noqa: E501

    :param categoria: search within a category (Vinhos de mesa, Espumantes, Uvas frescas, or Suco de uva)
    :type categoria: str
    :param pais: search for a country name
    :type pais: str
    :param ano: search for a specific year
    :type ano: str

    :rtype: List[ExportacaoItem]
    """

    result = []

    match categoria:
        case 'Vinhos de mesa':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv")
        case 'Espumantes':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv")
        case 'Uvas frescas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv")
        case 'Suco de uva':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv")
            
    data = pd.read_csv(file, sep=';')

    all_country_info = data[data['País'] == pais]

    if ano is None:
        for index, year in enumerate(all_country_info):
            if index >= 2:
                if ".1" not in year:
                    quantity = all_country_info[year].values[0]
                    value = all_country_info[year + '.1'].values[0]

                    item = ExportacaoItem(pais=pais,
                                        ano=int(year),
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

                    result.append(item)
    else:
        quantity = all_country_info[ano].values[0]
            
        if ".1" not in ano:
            quantity = all_country_info[ano].values[0]
            value = all_country_info[ano + '.1'].values[0]

            item = ExportacaoItem(pais=pais,
                                        ano=int(ano),
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

            result.append(item)
    return result


def search_importacao(categoria, pais, ano=None):  # noqa: E501
    """searches Importacao

    By passing in the appropriate options, you can search for available Importacao info in the system  # noqa: E501

    :param categoria: search within a category (Vinhos de mesa, Espumantes, Uvas frescas, or Suco de uva)
    :type categoria: str
    :param pais: search for a country name
    :type pais: str
    :param ano: search for a specific year
    :type ano: str

    :rtype: List[ImportacaoItem]
    """

    result = []

    match categoria:
        case 'Vinhos de mesa':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv")
        case 'Espumantes':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv")
        case 'Uvas frescas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv")
        case 'Uvas passas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv")
        case 'Suco de uva':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv")

    data = pd.read_csv(file, sep=';')

    all_country_info = data[data['País'] == pais]
    
    if ano is None:
        for index, ano in enumerate(all_country_info):
            if index >= 2:
                if ".1" not in ano:
                    quantity = all_country_info[ano].values[0]
                    value = all_country_info[ano + '.1'].values[0]
                    
                    item = ImportacaoItem(pais=pais,
                                        ano=int(ano),
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

                    result.append(item)
    else:
        quantity = all_country_info[ano].values[0]

        if ".1" not in ano:
            quantity = all_country_info[ano].values[0]
            value = all_country_info[ano + '.1'].values[0]

            item = ImportacaoItem(pais=pais,
                                        ano=ano,
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

            result.append(item)
    return result


def search_processamento(categoria, cultivar, ano=None):  # noqa: E501
    """searches Processamento

    By passing in the appropriate options, you can search for available Processamento info in the system  # noqa: E501

    :param categoria: search within a category (Viniferas, Americanas e Hibridas, Uvas de mesa, or Sem classificacao)
    :type categoria: str
    :param cultivar: search for a cultivar name
    :type cultivar: str
    :param ano: search for a specific year
    :type ano: str

    :rtype: List[ProcessamentoItem]
    """

    result = []

    match categoria:
        case 'Viniferas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv")
        case 'Americanas e Hibridas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv")
        case 'Uvas de mesa':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv")
        case 'Sem classificacao':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv")

    data = pd.read_csv(file, sep='\t')
        
    all_crop_info = data[data['cultivar'] == cultivar]

    if ano is None:
        for index, year in enumerate(all_crop_info):
            if index >= 3:
                crop = all_crop_info['cultivar'].values[0]
                quantity = all_crop_info[year].values[0]

                if isinstance(quantity, str) == True:
                    continue
                else:
                    item = ProcessamentoItem(categoria=categoria,
                                                        cultivar=crop,
                                                        ano=int(year),
                                                        quantidade=int(quantity)
                                                        ).to_dict()

                result.append(item)
    else:
        crop = all_crop_info['cultivar'].values[0]
        quantity = all_crop_info[ano].values[0]

        if isinstance(quantity, str) == True:
            pass
        else:
            item = ProcessamentoItem(categoria=categoria,
                                                cultivar=crop,
                                                ano=int(ano),
                                                quantidade=int(quantity)
                                                ).to_dict()

            result.append(item)
    return result


def search_producao(produto, ano=None):  # noqa: E501
    """searches Producao

    By passing in the appropriate options, you can search for available Producao info in the system  # noqa: E501

    :param produto: search for a product name
    :type produto: str
    :param ano: search for a specific year
    :type ano: str

    :rtype: List[ProducaoItem]
    """

    result = []

    file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")

    data = pd.read_csv(file, sep=';')
        
    all_product_info = data[data['produto'] == produto]

    if ano is None:
        for index, year in enumerate(all_product_info):
            if index >= 3:
                quantity = all_product_info[year].values[0]

                item = ProducaoItem(produto=produto,
                                    ano=int(year),
                                    quantidade=int(quantity)
                                    ).to_dict()

                result.append(item)
    else:
        quantity = all_product_info[ano].values[0]

        item = ProducaoItem(produto=produto,
                                        ano=int(ano),
                                        quantidade=int(quantity)
                                        ).to_dict()

        result.append(item)
    return result