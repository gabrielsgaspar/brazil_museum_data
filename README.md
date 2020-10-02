Brazil Museum Data Scrapper
===========================

[![Python 3.7](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/downloads/release/python-376/)
[![BSD License](http://img.shields.io/badge/license-MIT-green.svg)](https://github.com/gabrielsgaspar/brazil_museum_data/blob/main/LICENSE)
[![Commit](https://img.shields.io/github/last-commit/gabrielsgaspar/brazil_museum_data)](https://github.com/gabrielsgaspar/brazil_museum_data/commits/main)


This repo contains code to scrape all the data from Brazilian Museums that use [Tainacan](https://www.tainacan.org). It goes over each museum listed in the [Ibram website](https://www.museus.gov.br/acoes-e-programas/projeto-tainacan/) and loops through each available page of the Tainacan API. It then saves the data as a ```.csv``` file in the ```data/[MUSEUM]``` folder.

This script is written in python, so in order to execute it, install all the required libraries:

```sh
pip install -r requirements.txt
```

In order to execute the scrapper, go to the ```scrape``` folder and execute the following:

```sh
python3 scrape.py
```

All the data will be saved in the ```data``` folder.

The repo has the following structure:

```sh
.
├── LICENSE
├── README.md
├── data
│   ├── Museu_Casa_Histórica_de_Alcantara
│   │   └── raw.csv
│   ├── Museu_Casa_da_Hera
│   │   └── raw.csv
│   ├── Museu_Casa_de_Benjamin_Constant
│   │   └── raw.csv
│   ├── Museu_Historico_Nacional
│   │   └── raw.csv
│   ├── Museu_Regional_Casa_dos_Ottoni
│   │   └── raw.csv
│   ├── Museu_Regional_de_Sao_Joao_del-Rei
│   │   └── raw.csv
│   ├── Museu_Victor_Meirelles
│   │   └── raw.csv
│   ├── Museu_Villa_Lobos
│   │   └── raw.csv
│   ├── Museu_da_Bandeiras
│   │   └── raw.csv
│   ├── Museu_da_Inconfidencia
│   │   └── raw.csv
│   ├── Museu_das_Missoes
│   │   └── raw.csv
│   ├── Museu_de_Arqueologia_de_Itaipu
│   │   └── raw.csv
│   ├── Museu_de_Arte_Sacra_da_Boa_Morte
│   │   └── raw.csv
│   ├── Museu_do_Diamante
│   │   └── raw.csv
│   └── Museu_do_Ouro
│       └── raw.csv
├── requirements.txt
└── scrape
    └── scrape.py
```

If you find any bugs with the code, please [raise an issue](https://github.com/gabrielsgaspar/brazil_museum_data/issues/new).

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for further details.
