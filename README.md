# qr-code-generation

API para geração de QR Codes a partir de URLs, construída com FastAPI, seguindo boas práticas de modularização e extensibilidade. O projeto visa evoluir para coletar métricas de leitura dos QR Codes (dispositivo, local, horário).

## Funcionalidades

- Geração de QR Codes em PNG a partir de URLs válidas.
- API RESTful versionada.
- Estrutura modular para fácil manutenção e expansão.

## Como usar

### Instalação

```sh
make init
```

### Executando localmente

```sh
make running
```
Acesse: [http://localhost:8000/docs](http://localhost:8000/docs) para a documentação interativa (Swagger).

### Gerando QR Code

Faça um POST para `/api/v1/qr/generate` com o JSON:
```json
{
	"url": "https://exemplo.com"
}
```
A resposta será a imagem PNG do QR Code.

### Testes

```sh
make tests
```

### Formatação de código

```sh
make format
```

## Estrutura do Projeto

```
src/
	main.py                  # Entrypoint FastAPI
	qr_code_generation/
		api/qr_routes.py       # Endpoints da API
		core/generator.py      # Lógica de geração de QR Code
tests/                     # (vazio, pronto para testes)
Makefile                   # Comandos de build, run, test, format
```

## Convenções

- Python 3.12+, dependências via Poetry.
- Sempre use o prefixo `qr_code_generation` para imports internos.
- Rotas sempre versionadas: `/api/v1/qr`.
- Novos endpoints devem usar validação Pydantic e resposta tipada.

## Dependências principais

- FastAPI
- qrcode
- Pillow
- Pydantic
- Uvicorn

---

Sinta-se à vontade para adaptar conforme evoluir o projeto!