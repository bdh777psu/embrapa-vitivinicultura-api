import connexion
import six
import pandas as pd

from swagger_server.models.comercializacao_item import ComercializacaoItem  # noqa: E501
from swagger_server.models.exportacao_item import ExportacaoItem  # noqa: E501
from swagger_server.models.importacao_item import ImportacaoItem  # noqa: E501
from swagger_server.models.processamento_item import ProcessamentoItem  # noqa: E501
from swagger_server.models.producao_item import ProducaoItem  # noqa: E501
from swagger_server import util


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

    data = pd.read_csv('data/Comercio.csv', skipinitialspace=True, sep=';')
    
    all_product_info = data[data['Produto'] == comercializacao_product_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_product_info):
            if index >= 3:
                category = all_product_info['Categoria'].values[0]
                quantity = all_product_info[year].values[0]

                product_info = ComercializacaoItem(categoria=category,
                                    cultivar=comercializacao_product_search_string,
                                    ano=int(year),
                                    quantidade=int(quantity)
                                    ).to_dict()

                result.append(product_info)
    else:
        category = all_product_info['Categoria'].values[0]
        quantity = all_product_info[ano_search_string].values[0]
        
        product_info = ComercializacaoItem(categoria=category,
                                    cultivar=comercializacao_product_search_string,
                                    ano=int(ano_search_string),
                                    quantidade=int(quantity)
                                    ).to_dict()

        result.append(product_info)

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
            data = pd.read_csv('data/Exp/ExpVinho.csv', sep=';')
        case 'Espumantes':
            data = pd.read_csv('data/Exp/ExpEspumantes.csv', sep=';')
        case 'Uvas frescas':
            data = pd.read_csv('data/Exp/ExpUva.csv', sep=';')
        case 'Suco de uva':
            data = pd.read_csv('data/Exp/ExpSuco.csv', sep=';')

    all_country_info = data[data['País'] == exportacao_country_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_country_info):
            if index >= 2:
                if ".1" not in year:
                    quantity = all_country_info[year].values[0]
                    value = all_country_info[year + '.1'].values[0]

                    country_info = ExportacaoItem(pais=exportacao_country_search_string,
                                    ano=int(year),
                                    quantidade=int(quantity),
                                    valor=int(value)
                                    ).to_dict()

                    result.append(country_info)
    else:
        quantity = all_country_info[ano_search_string].values[0]
        
        if ".1" not in ano_search_string:
            quantity = all_country_info[ano_search_string].values[0]
            value = all_country_info[ano_search_string + '.1'].values[0]

            country_info = ExportacaoItem(pais=exportacao_country_search_string,
                                    ano=int(ano_search_string),
                                    quantidade=int(quantity),
                                    valor=int(value)
                                    ).to_dict()

            result.append(country_info)

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
            data = pd.read_csv('data/Imp/ImpVinhos.csv', sep=';')
        case 'Espumantes':
            data = pd.read_csv('data/Imp/ImpEspumantes.csv', sep=';')
        case 'Uvas frescas':
            data = pd.read_csv('data/Imp/Frescas.csv', sep=';')
        case 'Uvas passas':
            data = pd.read_csv('data/Imp/ImpPassas.csv', sep=';')
        case 'Suco de uva':
            data = pd.read_csv('data/Imp/ImpSuco.csv', sep=';')

    all_country_info = data[data['País'] == importacao_country_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_country_info):
            if index >= 2:
                if ".1" not in year:
                    quantity = all_country_info[year].values[0]
                    value = all_country_info[year + '.1'].values[0]

                    country_info = ImportacaoItem(pais=importacao_country_search_string,
                                    ano=int(year),
                                    quantidade=int(quantity),
                                    valor=int(value)
                                    ).to_dict()

                    result.append(country_info)
    else:
        quantity = all_country_info[ano_search_string].values[0]
        
        if ".1" not in ano_search_string:
            quantity = all_country_info[ano_search_string].values[0]
            value = all_country_info[ano_search_string + '.1'].values[0]

            country_info = ImportacaoItem(pais=importacao_country_search_string,
                                    ano=ano_search_string,
                                    quantidade=int(quantity),
                                    valor=int(value)
                                    ).to_dict()

            result.append(country_info)

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
            data = pd.read_csv('data/Processa/ProcessaViniferas.csv', sep='\t')
        case 'Americanas e Híbridas':
            data = pd.read_csv('data/Processa/ProcessaAmericanas.csv', sep='\t')
        case 'Uvas de mesa':
            data = pd.read_csv('data/Processa/ProcessaMesa.csv', sep='\t')
        case 'Sem classificação':
            data = pd.read_csv('data/Processa/ProcessaSemclass.csv', sep='\t')
    
    all_crop_info = data[data['cultivar'] == processamento_product_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_crop_info):
            if index >= 3:
                crop = all_crop_info['cultivar'].values[0]
                quantity = all_crop_info[year].values[0]

                if isinstance(quantity, str) == True:
                    continue
                else:
                    product_info = ProcessamentoItem(categoria=processamento_category_search_string,
                                                     cultivar=crop,
                                                     ano=int(year),
                                                     quantidade=int(quantity)
                                                     ).to_dict()

                    result.append(product_info)
    else:
        crop = all_crop_info['cultivar'].values[0]
        quantity = all_crop_info[ano_search_string].values[0]

        if isinstance(quantity, str) == True:
            pass
        else:
            product_info = ProcessamentoItem(categoria=processamento_category_search_string,
                                             cultivar=crop,
                                             ano=int(ano_search_string),
                                             quantidade=int(quantity)
                                             ).to_dict()

            result.append(product_info)

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

    data = pd.read_csv('data/Producao.csv', sep=';')
    
    all_product_info = data[data['produto'] == produto_search_string]

    if ano_search_string is None:
        for index, year in enumerate(all_product_info):
            if index >= 2:
                quantity = all_product_info[year].values[0]

                product_info = ProducaoItem(produto=produto_search_string,
                                    ano=int(year),
                                    quantidade=int(quantity)
                                    ).to_dict()

                result.append(product_info)
    else:
        quantity = all_product_info[ano_search_string].values[0]

        product_info = ProducaoItem(produto=produto_search_string,
                                    ano=int(ano_search_string),
                                    quantidade=int(quantity)
                                    ).to_dict()

        result.append(product_info)

    return result