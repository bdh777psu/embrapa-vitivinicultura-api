import connexion
import six

from swagger_server.models.comercializacao_item import ComercializacaoItem  # noqa: E501
from swagger_server.models.exportacao_item import ExportacaoItem  # noqa: E501
from swagger_server.models.importacao_item import ImportacaoItem  # noqa: E501
from swagger_server.models.processamento_item import ProcessamentoItem  # noqa: E501
from swagger_server.models.producao_item import ProducaoItem  # noqa: E501
from swagger_server import util


def search_comercializacao(produto_search_string, ano_search_string=None):  # noqa: E501
    """searches comercializacao

    By passing in the appropriate options, you can search for available comercializacao info in the system  # noqa: E501

    :param produto_search_string: pass a product name search string for looking up comercializacao
    :type produto_search_string: str
    :param ano_search_string: pass a year search string for looking up comercializacao
    :type ano_search_string: int

    :rtype: List[ComercializacaoItem]
    """
    return 'do some magic!'


def search_exportacao(processamento_category_search_string, processamento_product_search_string=None, ano_search_string=None):  # noqa: E501
    """searches exportacao

    By passing in the appropriate options, you can search for available exportacao info in the system  # noqa: E501

    :param processamento_category_search_string: pass a category name search string for looking up exportacao
    :type processamento_category_search_string: str
    :param processamento_product_search_string: pass a product name search string for looking up exportacao
    :type processamento_product_search_string: str
    :param ano_search_string: pass a year search string for looking up exportacao
    :type ano_search_string: int

    :rtype: List[ExportacaoItem]
    """
    return 'do some magic!'


def search_importacao(processamento_category_search_string, processamento_product_search_string=None, ano_search_string=None):  # noqa: E501
    """searches importacao

    By passing in the appropriate options, you can search for available importacao info in the system  # noqa: E501

    :param processamento_category_search_string: pass a category name search string for looking up importacao
    :type processamento_category_search_string: str
    :param processamento_product_search_string: pass a product name search string for looking up importacao
    :type processamento_product_search_string: str
    :param ano_search_string: pass a year search string for looking up importacao
    :type ano_search_string: int

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
    :type ano_search_string: int

    :rtype: List[ProcessamentoItem]
    """
    return 'do some magic!'


def search_producao(produto_search_string, ano_search_string=None):  # noqa: E501
    """searches producao

    By passing in the appropriate options, you can search for available producao info in the system  # noqa: E501

    :param produto_search_string: pass a product name search string for looking up producao
    :type produto_search_string: str
    :param ano_search_string: pass a year search string for looking up producao
    :type ano_search_string: int

    :rtype: List[ProducaoItem]
    """
    return 'do some magic!'
