#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This scripts downloads all the available data for each Brazilian museums that use
Tainacam as a service to host their collection. The list of available museums
is available in the README.md file of this repo. The outputs of this script are
unique .csv files per available museum with all flatten information.

By: @gabrielsgaspar
"""

# Import necessary libraries
import os, json, requests
import pandas as pd
import numpy as np
from flatten_json import flatten

# Set up url handle of apis for museums that use Tainacam as dictionary
museums = {
            "Museu_Historico_Nacional": ("http://mhn.acervos.museus.gov.br", 24),
            "Museu_do_Diamante": ("https://museudodiamante.acervos.museus.gov.br", 11603),
            "Museu_do_Ouro": ("https://museudoouro.acervos.museus.gov.br", 3583),
            "Museu_Victor_Meirelles": ("http://museuvictormeirelles.acervos.museus.gov.br", 18004),
            "Museu_Regional_Casa_dos_Ottoni": ("https://museuregionalcasadosottoni.acervos.museus.gov.br", 31492),
            "Museu_de_Arqueologia_de_Itaipu": ("http://museudearqueologiadeitaipu.museus.gov.br", 94553),
            "Museu_das_Missoes": ("http://museudasmissoes.acervos.museus.gov.br", 6409),
            "Museu_da_Bandeiras": ("http://museusibramgoias.acervos.museus.gov.br", 1093),
            "Museu_Villa_Lobos": ("http://museuvillalobos.acervos.museus.gov.br", 1570),
            "Museu_Casa_de_Benjamin_Constant": ("http://museucasabenjaminconstant.acervos.museus.gov.br", 5347),
            "Museu_da_Inconfidencia": ("http://museudainconfidencia.acervos.museus.gov.br", 9),
            "Museu_Regional_de_Sao_Joao_del-Rei": ("http://museuregionaldesaojoaodelrei.acervos.museus.gov.br", 11451),
            "Museu_de_Arte_Sacra_da_Boa_Morte": ("http://museusibramgoias.acervos.museus.gov.br", 3387),
            "Museu_Casa_da_Hera": ("http://museucasadahera.acervos.museus.gov.br", 7),
            "Museu_Casa_Histórica_de_Alcantara": ("http://museucasahistoricadealcantara.acervos.museus.gov.br/", 14284)

        }
