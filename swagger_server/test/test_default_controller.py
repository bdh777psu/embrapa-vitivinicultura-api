# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comercializacao_item import ComercializacaoItem  # noqa: E501
from swagger_server.models.exportacao_item import ExportacaoItem  # noqa: E501
from swagger_server.models.importacao_item import ImportacaoItem  # noqa: E501
from swagger_server.models.processamento_item import ProcessamentoItem  # noqa: E501
from swagger_server.models.producao_item import ProducaoItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_search_comercializacao(self):
        """Test case for search_comercializacao

        searches comercializacao
        """
        query_string = [('comercializacao_product_search_string', 'comercializacao_product_search_string_example'),
                        ('ano_search_string', 'ano_search_string_example')]
        response = self.client.open(
            '/comercializacao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_exportacao(self):
        """Test case for search_exportacao

        searches exportacao
        """
        query_string = [('exportacao_category_search_string', 'exportacao_category_search_string_example'),
                        ('exportacao_country_search_string', 'exportacao_country_search_string_example'),
                        ('ano_search_string', 'ano_search_string_example')]
        response = self.client.open(
            '/exportacao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_importacao(self):
        """Test case for search_importacao

        searches importacao
        """
        query_string = [('importacao_category_search_string', 'importacao_category_search_string_example'),
                        ('importacao_country_search_string', 'importacao_country_search_string_example'),
                        ('ano_search_string', 'ano_search_string_example')]
        response = self.client.open(
            '/importacao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_processamento(self):
        """Test case for search_processamento

        searches processamento
        """
        query_string = [('processamento_category_search_string', 'processamento_category_search_string_example'),
                        ('processamento_product_search_string', 'processamento_product_search_string_example'),
                        ('ano_search_string', 'ano_search_string_example')]
        response = self.client.open(
            '/processamento',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_producao(self):
        """Test case for search_producao

        searches producao
        """
        query_string = [('produto_search_string', 'produto_search_string_example'),
                        ('ano_search_string', 'ano_search_string_example')]
        response = self.client.open(
            '/producao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
