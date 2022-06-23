# ALGOSUP_2022_Project_5_F

The goal of this project is to create an AI to understand human language. the AI have to detect wether people around are talking french or english during project time.

<hr>

<details><summary>Table of content</summary>

- [ALGOSUP_2022_Project_5_F](#algosup_2022_project_5_f)
  - [1. How does our AI works ?](#1-how-does-our-ai-works-)
  - [2. What do we use ?](#2-what-do-we-use-)
  - [3. Usage](#3-usage)
</details>

<hr>

## 1. How does our AI works ?

Firstly we had to import datasets, we currently have two datasets, one with english voices (70GB) and a second one with french voices (50GB).

Thanks to these datasets we can train or AI, to do that we are using [google colab](https://colab.research.google.com/?hl=en), it is a website where we can create ou AI in python and use Google's GPUs to to train and test it with datasets before using it in real situation.

Then we transform audio files and recorded voices into a spectogram, it is a representation of sound in images. The AI can finally search for patterns inside theses images and sort languagues between french and english.

Our program will output the proobabilities of English and French.

## 2. What do we use ?

As said before we are using two [Datasets from Mozilla](https://commonvoice.mozilla.org/en/datasets), the English one and the French one.

We are also using [Google colab](https://colab.research.google.com/?hl=en) for writing and traing our Model.

We are using an [Raspeberry PI 4 model B](https://fr.rs-online.com/web/p/raspberry-pi/1822098?cm_mmc=FR-PPC-DS3A-_-google-_-3_FR_FR_MPN_Raspberry+Pi+%26+Arduino+%26+Outils+de+d%C3%A9veloppement_Raspberry+Pi_Exact-_-Raspberry+Pi+-+1822098+-+Raspberry+Pi+4+8G+Model+B-_-raspberry+pi+4+8g+model+b&matchtype=e&aud-827186183686:kwd-911155539340&gclid=Cj0KCQjwhLKUBhDiARIsAMaTLnHnLZkA9mBSBhKMJNn7Jk8OqPQ4bivH10LQnhWVOGP6PPHJ8np7k_IaAh-IEALw_wcB&gclsrc=aw.ds) to store the model and we are using the microphone to detect when someone is speaking

We are also using the Raspberry to host an Apache Web Server. 
It allows us to have a visual interface to see the results of our AI.

## 3. Usage

`cd predict`
`python test.py`
`python test.py ./FOLDER/`

