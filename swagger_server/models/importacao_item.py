# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ImportacaoItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pais: str=None, ano: int=None, quantidade: str=None):  # noqa: E501
        """ImportacaoItem - a model defined in Swagger

        :param pais: The pais of this ImportacaoItem.  # noqa: E501
        :type pais: str
        :param ano: The ano of this ImportacaoItem.  # noqa: E501
        :type ano: int
        :param quantidade: The quantidade of this ImportacaoItem.  # noqa: E501
        :type quantidade: str
        """
        self.swagger_types = {
            'pais': str,
            'ano': int,
            'quantidade': str
        }

        self.attribute_map = {
            'pais': 'pais',
            'ano': 'ano',
            'quantidade': 'quantidade'
        }
        self._pais = pais
        self._ano = ano
        self._quantidade = quantidade

    @classmethod
    def from_dict(cls, dikt) -> 'ImportacaoItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImportacaoItem of this ImportacaoItem.  # noqa: E501
        :rtype: ImportacaoItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pais(self) -> str:
        """Gets the pais of this ImportacaoItem.


        :return: The pais of this ImportacaoItem.
        :rtype: str
        """
        return self._pais

    @pais.setter
    def pais(self, pais: str):
        """Sets the pais of this ImportacaoItem.


        :param pais: The pais of this ImportacaoItem.
        :type pais: str
        """
        if pais is None:
            raise ValueError("Invalid value for `pais`, must not be `None`")  # noqa: E501

        self._pais = pais

    @property
    def ano(self) -> int:
        """Gets the ano of this ImportacaoItem.


        :return: The ano of this ImportacaoItem.
        :rtype: int
        """
        return self._ano

    @ano.setter
    def ano(self, ano: int):
        """Sets the ano of this ImportacaoItem.


        :param ano: The ano of this ImportacaoItem.
        :type ano: int
        """
        if ano is None:
            raise ValueError("Invalid value for `ano`, must not be `None`")  # noqa: E501

        self._ano = ano

    @property
    def quantidade(self) -> str:
        """Gets the quantidade of this ImportacaoItem.


        :return: The quantidade of this ImportacaoItem.
        :rtype: str
        """
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: str):
        """Sets the quantidade of this ImportacaoItem.


        :param quantidade: The quantidade of this ImportacaoItem.
        :type quantidade: str
        """
        if quantidade is None:
            raise ValueError("Invalid value for `quantidade`, must not be `None`")  # noqa: E501

        self._quantidade = quantidade
