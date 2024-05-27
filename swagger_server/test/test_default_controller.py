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

        searches Comercializacao
        """
        query_string = [('produto', 'produto_example'),
                        ('ano', 'ano_example')]
        response = self.client.open(
            '/comercializacao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_exportacao(self):
        """Test case for search_exportacao

        searches Exportacao
        """
        query_string = [('categoria', 'categoria_example'),
                        ('pais', 'pais_example'),
                        ('ano', 'ano_example')]
        response = self.client.open(
            '/exportacao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_importacao(self):
        """Test case for search_importacao

        searches Importacao
        """
        query_string = [('categoria', 'categoria_example'),
                        ('pais', 'pais_example'),
                        ('ano', 'ano_example')]
        response = self.client.open(
            '/importacao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_processamento(self):
        """Test case for search_processamento

        searches Processamento
        """
        query_string = [('categoria', 'categoria_example'),
                        ('cultivar', 'cultivar_example'),
                        ('ano', 'ano_example')]
        response = self.client.open(
            '/processamento',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_producao(self):
        """Test case for search_producao

        searches Producao
        """
        query_string = [('produto', 'produto_example'),
                        ('ano', 'ano_example')]
        response = self.client.open(
            '/producao',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
