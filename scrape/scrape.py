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
import os, json, requests, time
import pandas as pd
import numpy as np
from flatten_json import flatten
from tqdm.auto import tqdm

# Define function to check if data folders exist
def data_folder(museums):
    """
    This function verifies if a folder exists for each museum in the argument as key
    and creates one in case folder is missing.

    Argument:
        museums: a dictionary with museum names as keys and a tuple containing the
                 address as the first argument and Tainacam collection as the second
    Output:
        ../data/[MUSEM]: a folder for each museum in argument

    """
    # Set loop to check if folder exists for each museum
    for museum in museums:
        if not os.path.exists('../data/{}'.format(museum.replace(" ", "_").lower())):
            os.makedirs('../data/{}'.format(museum.replace(" ", "_").lower()))

# Define function to download all museum data
def download_museum(museums):
    """
    This function downloads all the data available for the museums in the Ibram
    website that use Tainacam as a platform to host their APIs.

    Argument:
        museums: a dictionary with museum names as keys and a tuple containing the
                 address as the first argument and Tainacam collection as the second
    Output:
        museum_data: a .csv file with all the available data for the museums

    """
    # Loop through museums and retrieve all available data
    for museum in tqdm(museums):
        # Set initial value for page and dataframe to hold museum data
        page = 1
        museum_data = pd.DataFrame()
        # Loop until page is retrieved as empty
        while True:
            # Make request to the API and load data as json
            request = requests.get("{}/wp-json/tainacan/v2/collection/{}/items/?perpage=96&order=DESC&orderby=date&paged={}".format(museums[museum][0], museums[museum][1], page))
            json_data = json.loads(request.text)
            # Break out of the loop if result is empty, ie. last page has been reached
            if len(json_data["items"]) == 0:
                break
            # Flatten json, normalize as dataframe and assign it to dataframe
            flat_json = flatten(json_data)
            page_data = pd.json_normalize(flat_json)
            # Append page data to dataframe for museum data
            museum_data = museum_data.append(page_data, ignore_index = True, sort = False)
            # Increase page count for next loop
            page += 1
        # Save museum data in data/[MUSEUM] folder
        museum_data.to_csv("../data/{}/raw.csv".format(museum.replace(" ", "_").lower()), index = False, encoding = "utf-8-sig")

if __name__ == "__main__":
    # Print message for download
    print("Welcome to the Brazilian Museum scraper!\n")
    print("""\
                 ( (
                  ) )
                (----)-)
                 \__/-'
                `----'  @gabrielsgaspar
        """)
    # Set up url handle of apis for museums that use Tainacam as dictionary
    museums = {
                "Museu Historico Nacional": ("http://mhn.acervos.museus.gov.br", 24),
                "Museu do Diamante": ("https://museudodiamante.acervos.museus.gov.br", 11603),
                "Museu do Ouro": ("https://museudoouro.acervos.museus.gov.br", 3583),
                "Museu Victor Meirelles": ("http://museuvictormeirelles.acervos.museus.gov.br", 18004),
                "Museu Regional Casa dos Ottoni": ("https://museuregionalcasadosottoni.acervos.museus.gov.br", 31492),
                "Museu de Arqueologia de Itaipu": ("http://museudearqueologiadeitaipu.museus.gov.br", 94553),
                "Museu das Missoes": ("http://museudasmissoes.acervos.museus.gov.br", 6409),
                "Museu da Bandeiras": ("http://museusibramgoias.acervos.museus.gov.br", 1093),
                "Museu Villa Lobos": ("http://museuvillalobos.acervos.museus.gov.br", 1570),
                "Museu Casa de Benjamin_Constant": ("http://museucasabenjaminconstant.acervos.museus.gov.br", 5347),
                "Museu da Inconfidencia": ("http://museudainconfidencia.acervos.museus.gov.br", 9),
                "Museu Regional de Sao Joao del-Rei": ("http://museuregionaldesaojoaodelrei.acervos.museus.gov.br", 11451),
                "Museu de Arte Sacra da Boa Morte": ("http://museusibramgoias.acervos.museus.gov.br", 3387),
                "Museu Casa da Hera": ("http://museucasadahera.acervos.museus.gov.br", 7),
                "Museu Casa Histórica de Alcantara": ("http://museucasahistoricadealcantara.acervos.museus.gov.br/", 14284)
            }
    # Check if data directory exists for each museum
    print("Checking if data directories exist ...")
    data_folder(museums)
    time.sleep(2)
    # Call function to download data
    print("Downloading data ...")
    download_museum(museums)
    time.sleep(2)
    # Print complete message and exit
    print("Download of Brazilian museums done!")
