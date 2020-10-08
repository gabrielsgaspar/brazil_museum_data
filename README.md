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
├── museu_casa_da_hera
│   │   └── raw.csv
│   ├── museu_casa_de_benjamin_constant
│   │   └── raw.csv
│   ├── museu_casa_histórica_de_alcantara
│   │   └── raw.csv
│   ├── museu_da_bandeiras
│   │   └── raw.csv
│   ├── museu_da_inconfidencia
│   │   └── raw.csv
│   ├── museu_das_missoes
│   │   └── raw.csv
│   ├── museu_de_arqueologia_de_itaipu
│   │   └── raw.csv
│   ├── museu_de_arte_sacra_da_boa_morte
│   │   └── raw.csv
│   ├── museu_do_diamante
│   │   └── raw.csv
│   ├── museu_do_ouro
│   │   └── raw.csv
│   ├── museu_historico_nacional
│   │   └── raw.csv
│   ├── museu_regional_casa_dos_ottoni
│   │   └── raw.csv
│   ├── museu_regional_de_sao_joao_del-rei
│   │   └── raw.csv
│   ├── museu_victor_meirelles
│   │   └── raw.csv
│   └── museu_villa_lobos
│       └── raw.csv
├── requirements.txt
└── scrape
    └── scrape.py
```

If you find any bugs with the code, please [raise an issue](https://github.com/gabrielsgaspar/brazil_museum_data/issues/new).

This project is licensed under the MIT License and was made by [@gabrielsgaspar](https://github.com/gabrielsgaspar). See [LICENSE](LICENSE) file for further details.
