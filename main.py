import requests
from colorama import *
from utils import current_time, logstr
import json

WARNING_PREFIX = f"{Fore.YELLOW}(WARNING) {current_time()} ::"
ERROR_PREFIX = f"{Fore.RED}(ERROR) {current_time()} ::"
SUCCESS_PREFIX = f"{Fore.GREEN}(SUCCESS) {current_time()} ::"
INFO_PREFIX = f"{Fore.BLUE}(INFO) {current_time()} ::"


def make_request(url):
    logstr(f'{INFO_PREFIX} Testando URL: {url}')
    request_data = {}
    r = requests.get(url)
    request_data["time"] = r.elapsed.total_seconds()
    request_data["body"] = json.loads(r.text)
    request_data["status"] = r.status_code
    return request_data

def validate_request(request):
#Critérios fictícios de teste, dependendo da API ou do server HTTP eles podem ser diferentes e mais completos
    logstr(f'{INFO_PREFIX} Request Demorou {request["time"]} segundos ')

    if request["status"] != 200:
        logstr(f'{INFO_PREFIX} Status HTTP: f{request["status"]}')
    else:
        logstr(f'{SUCCESS_PREFIX} OK 200')

    if not request["body"]["data"]:
        logstr(f'{ERROR_PREFIX} Não respondeu com dados')

def request_and_validate(url):
    validate_request(make_request(url))
    logstr("")

def main():
    logstr(f'{INFO_PREFIX} Iniciando testes...')

    request_and_validate("https://reqres.in/api/users?page=2")
    #Página inválida por exemplo
    request_and_validate("https://reqres.in/api/users?page=253524")

if __name__ == "__main__":
    main()
