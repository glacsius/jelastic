from api.apirestplus import api

from api.endpoints.clientes import ns as ns_clientes
from api.endpoints.teste import ns as ns_testes
from api.endpoints.sistema_aks import ns as ns_sistema_aks


def add_namespaces():
    api.add_namespace(ns_clientes)
    api.add_namespace(ns_testes)
    api.add_namespace(ns_sistema_aks)
