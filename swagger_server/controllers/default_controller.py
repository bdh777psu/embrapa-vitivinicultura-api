import connexion
import six
import pandas as pd

from swagger_server.models.comercializacao_item import ComercializacaoItem  # noqa: E501
from swagger_server.models.exportacao_item import ExportacaoItem  # noqa: E501
from swagger_server.models.importacao_item import ImportacaoItem  # noqa: E501
from swagger_server.models.processamento_item import ProcessamentoItem  # noqa: E501
from swagger_server.models.producao_item import ProducaoItem  # noqa: E501
from swagger_server import util


def search_comercializacao(comercializacao_category_search_string, comercializacao_product_search_string=None, ano_search_string=None):  # noqa: E501
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
    return 'do some magic!'


def search_exportacao(exportacao_category_search_string, exportacao_product_search_string=None, ano_search_string=None):  # noqa: E501
    """searches exportacao

    By passing in the appropriate options, you can search for available exportacao info in the system  # noqa: E501

    :param exportacao_category_search_string: pass a category name search string for looking up exportacao
    :type exportacao_category_search_string: str
    :param exportacao_product_search_string: pass a product name search string for looking up exportacao
    :type exportacao_product_search_string: str
    :param ano_search_string: pass a year search string for looking up exportacao
    :type ano_search_string: str

    :rtype: List[ExportacaoItem]
    """
    return 'do some magic!'


def search_importacao(importacao_category_search_string, importacao_product_search_string=None, ano_search_string=None):  # noqa: E501
    """searches importacao

    By passing in the appropriate options, you can search for available importacao info in the system  # noqa: E501

    :param importacao_category_search_string: pass a category name search string for looking up importacao
    :type importacao_category_search_string: str
    :param importacao_product_search_string: pass a product name search string for looking up importacao
    :type importacao_product_search_string: str
    :param ano_search_string: pass a year search string for looking up importacao
    :type ano_search_string: str

    :rtype: List[ImportacaoItem]
    """
    return 'do some magic!'


def search_processamento(processamento_category_search_string, processamento_product_search_string=None, ano_search_string=None):  # noqa: E501
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

    data = pd.read_csv('data/ProcessaViniferas.csv', sep='\t')
    
    all_category_info = data[data['control'] == processamento_category_search_string]

    prefix = 'ti_' if processamento_category_search_string == 'TINTAS' else 'br_'

    if processamento_product_search_string is None and ano_search_string is None:
        for index, year in enumerate(all_category_info):
            if index >= 3:
                crop = all_category_info['cultivar'].values[0]
                quantity = all_category_info[year].values[0]

                if isinstance(quantity, str) == True:
                    continue
                else:
                    product_info = ProcessamentoItem(categoria=processamento_category_search_string,
                                                     cultivar=crop,
                                                     ano=int(year),
                                                     quantidade=int(quantity)
                                                     ).to_dict()

                    result.append(product_info)
    elif processamento_product_search_string is None and ano_search_string is not None:
        crop = all_category_info['cultivar'].values[0]
        quantity = all_category_info[ano_search_string].values[0]

        product_info = ProcessamentoItem(categoria=processamento_category_search_string,
                                             cultivar=crop,
                                             ano=ano_search_string,
                                             quantidade=int(quantity)
                                             ).to_dict()

        result.append(product_info)
        
    elif processamento_product_search_string is not None and ano_search_string is None:
        all_category_info = data[data['control'] == prefix + processamento_product_search_string]

        for index, year in enumerate(all_category_info):
            if index >= 3:
                crop = all_category_info['cultivar'].values[0]
                quantity = all_category_info[year].values[0]

                if isinstance(quantity, str) == True:
                    continue
                else:
                    product_info = ProcessamentoItem(categoria=processamento_category_search_string,
                                                     cultivar=crop,
                                                     ano=int(year),
                                                     quantidade=int(quantity)
                                                     ).to_dict()

                    result.append(product_info)

    elif processamento_product_search_string is not None and ano_search_string is not None:
        all_category_info = data[data['control'] == prefix + processamento_product_search_string]
        crop = all_category_info['cultivar'].values[0]
        quantity = all_category_info[ano_search_string].values[0]

        product_info = ProcessamentoItem(categoria=processamento_category_search_string,
                                             cultivar=crop,
                                             ano=ano_search_string,
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
                                    ano=ano_search_string,
                                    quantidade=int(quantity)
                                    ).to_dict()

        result.append(product_info)

    return result