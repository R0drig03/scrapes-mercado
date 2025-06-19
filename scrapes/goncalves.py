import requests

class ScrapeGoncalves:
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }
        
        self.__cookies = {
                "app": '{"cep":"76.901-154","cidade":24,"empresa":8,"tipoEnvio":1}'
            }
        self.categoria_produto = 'açougue'
        self.pagina = self.consultaPaginas() #-> ITENS SÃO LIMITADOS DE ACORDO COM A QUANTIDADE DE PÁGINAS
        
        self.url = f'https://www.irmaosgoncalves.com.br/api/produto/pesquisar?&categoria=/categoria/{self.categoria_produto}&pagina={self.pagina}'


    def consultaPaginas(self) -> int: #MÉTODO PARA DESCOBRIR A QUANTIDADE TOTAL DE PÁGINAS
        
        url = 'https://www.irmaosgoncalves.com.br/api/produto/pesquisar?&categoria=/categoria/açougue&pagina=1'
        response = requests.get(url, headers=self.headers, cookies=self.__cookies)
        if response.status_code == 200:
            data = response.json()
            return data.get('paginas')
        
        print(f"Erro ao acessar API Gonçalves: {response.status_code}")


    def consultaCarnes(self):
        if self.pagina and self.pagina > 0:  
            response = requests.get(self.url, headers=self.headers, cookies=self.__cookies)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Erro ao acessar API Gonçalves: {response.status_code}")
                
        print(f"Nenhuma página encontrada")
    
    
         
         
    

