# OPIM244Project

## Setup


Create and activate a virtual environment:

```sh
conda create -n kiwi-env python=3.8

conda activate kiwi-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage (i.e. `ALPHAVANTAGE_API_KEY`).



Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"

```


## Usage

Run an example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python -m app.unemployment
```

Run stocks report:

```sh
python -m app.stocks
```


### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```


## Testing

Run tests:

```sh
pytest
```
