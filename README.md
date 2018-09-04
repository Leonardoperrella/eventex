# Eventex

Sistema de Eventos encomendado pela Morena

## Como desenvolver


1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com .env
6. Execute os testes.

```console
git clone git@github.com:Leonardoperrella/Eventex.git wttd
cd wttd
python -m venv .wttd
Scripts/Activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

```


## Como fazer o deploy

1. Crie uma instancia no heroku.
2. Envie as configurações para o keroku
3. Defina uma SECRET_KEY para instância.
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY="python contrib/secret_gen.py" 
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force



```

"# eventex" 
