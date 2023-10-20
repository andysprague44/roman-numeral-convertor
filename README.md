# Roman Number Convertor

This repository contains basic flask app for a pair programming exercise to build out a roman numeral convertion tool.

## Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/andysprague44/roman-numeral-convertor.git
$ cd roman-numeral-convertor
$ python -m venv myenv
$ source myenv/bin/activate #or, myenv/Scripts/activate
$ pip3 install -r requirements.txt
$ flask run
```

**Installation via `conda`**:

```shell
$ git clone https://github.com/andysprague44/roman-numeral-convertor.git 
$ cd roman-numeral-convertor
$ conda env create --force -f environment.yml
$ conda activate roman
$ flask run
```

## Usage

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application (should be `wsgi.py`).
* `FLASK_ENV`: The environment to run your app in (either `development` or `production`).
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `LESS_BIN`: Path to your local LESS installation via `which lessc` (optional for static assets).
* `ASSETS_DEBUG`: Debug asset creation and bundling in `development` (optional).
* `LESS_RUN_IN_DEBUG`: Debug LESS while in `development` (optional).
* `COMPRESSOR_DEBUG`: Debug asset compression while in `development` (optional).

*Remember never to commit secrets saved in .env files to Github.*

-----
