

class ExtratorURL():
    def __init__(self, url):
        self.url = url.strip() if type(url) == str else ""
        self.valida_url()

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        valor = self.get_url_parametros()[indice_valor:] if indice_e_comercial == -1 else self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)