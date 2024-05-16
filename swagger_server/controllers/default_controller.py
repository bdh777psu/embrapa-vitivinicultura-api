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
    response = requests.get(url)
    
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        save_path = os.path.join("data/", file_name)

        with open(save_path, 'wb') as file:
            file.write(response.content)
    
        return save_path
    else:
        print("Error: " + str(response.status_code))

def search_comercializacao(comercializacao_product_search_string, ano_search_string=None):  # noqa: E501
    """searches comercializacao

    By passing in the appropriate options, you can search for available comercializacao info in the system  # noqa: E501

    :param comercializacao_category_search_string: pass a category name search string for looking up comercializacao
    :type comercializacao_category_search_string: str
    :param comercializacao_product_search_string: pass a product name search string for looking up comercializacao
    :type comercializacao_product_search_string: str
    :param ano_search_string: pass a year search string for looking up comercializacao
    :type ano_search_string: str

    :rtype: List[ComercializacaoItem]
    """

    result = []

    file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv")
    data = pd.read_csv(file, sep=';')
        
    all_product_info = data[data['Produto'] == comercializacao_product_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_product_info):
            if index >= 3:
                product = all_product_info['Produto'].values[0]
                quantity = all_product_info[year].values[0]

                item = ComercializacaoItem(categoria=product,
                                        cultivar=comercializacao_product_search_string,
                                        ano=int(year),
                                        quantidade=int(quantity)
                                        ).to_dict()

                result.append(item)
    else:
        product = all_product_info['Produto'].values[0]
        quantity = all_product_info[ano_search_string].values[0]
                
        item = ComercializacaoItem(categoria=product,
                                        cultivar=comercializacao_product_search_string,
                                        ano=int(ano_search_string),
                                        quantidade=int(quantity)
                                        ).to_dict()

        result.append(item)
    return result


def search_exportacao(exportacao_category_search_string, exportacao_country_search_string, ano_search_string=None):  # noqa: E501
    """searches exportacao

    By passing in the appropriate options, you can search for available exportacao info in the system  # noqa: E501

    :param exportacao_category_search_string: pass a category name search string for looking up exportacao
    :type exportacao_category_search_string: str
    :param exportacao_country_search_string: pass a country name search string for looking up exportacao
    :type exportacao_country_search_string: str
    :param ano_search_string: pass a year search string for looking up exportacao
    :type ano_search_string: str

    :rtype: List[ExportacaoItem]
    """

    result = []

    match exportacao_category_search_string:
        case 'Vinhos de mesa':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv")
        case 'Espumantes':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv")
        case 'Uvas frescas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv")
        case 'Suco de uva':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv")
            
    data = pd.read_csv(file, sep=';')

    all_country_info = data[data['País'] == exportacao_country_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_country_info):
            if index >= 2:
                if ".1" not in year:
                    quantity = all_country_info[year].values[0]
                    value = all_country_info[year + '.1'].values[0]

                    item = ExportacaoItem(pais=exportacao_country_search_string,
                                        ano=int(year),
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

                    result.append(item)
    else:
        quantity = all_country_info[ano_search_string].values[0]
            
        if ".1" not in ano_search_string:
            quantity = all_country_info[ano_search_string].values[0]
            value = all_country_info[ano_search_string + '.1'].values[0]

            item = ExportacaoItem(pais=exportacao_country_search_string,
                                        ano=int(ano_search_string),
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

            result.append(item)
    return result


def search_importacao(importacao_category_search_string, importacao_country_search_string, ano_search_string=None):  # noqa: E501
    """searches importacao

    By passing in the appropriate options, you can search for available importacao info in the system  # noqa: E501

    :param importacao_category_search_string: pass a category name search string for looking up importacao
    :type importacao_category_search_string: str
    :param importacao_country_search_string: pass a country name search string for looking up importacao
    :type importacao_country_search_string: str
    :param ano_search_string: pass a year search string for looking up importacao
    :type ano_search_string: str

    :rtype: List[ImportacaoItem]
    """

    result = []

    match importacao_category_search_string:
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

    all_country_info = data[data['País'] == importacao_country_search_string]
    
    if ano_search_string is None:
        for index, year in enumerate(all_country_info):
            if index >= 2:
                if ".1" not in year:
                    quantity = all_country_info[year].values[0]
                    value = all_country_info[year + '.1'].values[0]
                    
                    item = ImportacaoItem(pais=importacao_country_search_string,
                                        ano=int(year),
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

                    result.append(item)
    else:
        quantity = all_country_info[ano_search_string].values[0]

        if ".1" not in ano_search_string:
            quantity = all_country_info[ano_search_string].values[0]
            value = all_country_info[ano_search_string + '.1'].values[0]

            item = ImportacaoItem(pais=importacao_country_search_string,
                                        ano=ano_search_string,
                                        quantidade=int(quantity),
                                        valor=int(value)
                                        ).to_dict()

            result.append(item)
    return result


def search_processamento(processamento_category_search_string, processamento_product_search_string, ano_search_string=None):  # noqa: E501
    """searches processamento

    By passing in the appropriate options, you can search for available processamento info in the system  # noqa: E501

    :param processamento_category_search_string: pass a category name search string for looking up processamento
    :type processamento_category_search_string: str
    :param processamento_product_search_string: pass a product name search string for looking up processamento
    :type processamento_product_search_string: str
    :param ano_search_string: pass a year search string for looking up processamento
    :type ano_search_string: str

    :rtype: List[ProcessamentoItem]
    """

    result = []

    match processamento_category_search_string:
        case 'Viníferas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv")
        case 'Americanas e Híbridas':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv")
        case 'Uvas de mesa':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv")
        case 'Sem classificação':
            file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv")

    data = pd.read_csv(file, sep='\t')
        
    all_crop_info = data[data['cultivar'] == processamento_product_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_crop_info):
            if index >= 3:
                crop = all_crop_info['cultivar'].values[0]
                quantity = all_crop_info[year].values[0]

                if isinstance(quantity, str) == True:
                    continue
                else:
                    item = ProcessamentoItem(categoria=processamento_category_search_string,
                                                        cultivar=crop,
                                                        ano=int(year),
                                                        quantidade=int(quantity)
                                                        ).to_dict()

                result.append(item)
    else:
        crop = all_crop_info['cultivar'].values[0]
        quantity = all_crop_info[ano_search_string].values[0]

        if isinstance(quantity, str) == True:
            pass
        else:
            item = ProcessamentoItem(categoria=processamento_category_search_string,
                                                cultivar=crop,
                                                ano=int(ano_search_string),
                                                quantidade=int(quantity)
                                                ).to_dict()

            result.append(item)
    return result


def search_producao(produto_search_string, ano_search_string=None):  # noqa: E501
    """searches producao

    By passing in the appropriate options, you can search for available producao info in the system  # noqa: E501

    :param produto_search_string: pass a product name search string for looking up producao
    :type produto_search_string: str
    :param ano_search_string: pass a year search string for looking up producao
    :type ano_search_string: str

    :rtype: List[ProducaoItem]
    """

    result = []

    file = download_csv("http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv")

    data = pd.read_csv(file, sep=';')
        
    all_product_info = data[data['produto'] == produto_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_product_info):
            if index >= 3:
                quantity = all_product_info[year].values[0]

                item = ProducaoItem(produto=produto_search_string,
                                    ano=int(year),
                                    quantidade=int(quantity)
                                    ).to_dict()

                result.append(item)
    else:
        quantity = all_product_info[ano_search_string].values[0]

        item = ProducaoItem(produto=produto_search_string,
                                        ano=int(ano_search_string),
                                        quantidade=int(quantity)
                                        ).to_dict()

        result.append(item)
    return result