import requests

class CalculadoraRest:

     # Construtor da classe
    def __init__(self, base_url):
        self.base_url = base_url

    def operacao(self, param1, param2, operacao):
        url = f"{self.base_url}/{operacao}/{param1}/{param2}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('result')
        else:
            return f"Erro: {response.status_code}, {response.text}"
            

    def soma(self, param1, param2, operacao):

        return self.operacao(param1, param2, operacao)

    def subtracao(self, param1, param2, operacao):

        return self.operacao(param1, param2, operacao)

    def multiplicacao(self, param1, param2, operacao):

        return self.operacao(param1, param2, operacao)

    def divisao(self, param1, param2, operacao):

        return self.operacao(param1, param2, operacao)


if __name__ == "__main__":
    calculadora = CalculadoraRest("http://localhost:8080/operation")

    # Exemplo de uso:
    print("Soma: 10 + 5 =", calculadora.soma(10, 5, "soma"))
    print("Subtracao: 10 - 5 =", calculadora.subtracao(10, 5, "subtracao"))
    print("Divisao: 10/5 =", calculadora.divisao(10, 5, "divisao"))
    print("Multiplicacao: 10*5 =", calculadora.multiplicacao(10, 5, "multiplicacao"))
   