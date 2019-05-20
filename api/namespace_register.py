from api.apirestplus import api

from api.endpoints.clientes import ns as ns_clientes
from api.endpoints.teste import ns as ns_testes


def add_namespaces():
    api.add_namespace(ns_clientes)
    api.add_namespace(ns_testes)
