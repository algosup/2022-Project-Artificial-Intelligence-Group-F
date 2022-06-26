# ALGOSUP_2022_Project_5_F

The goal of this project is to create an AI to understand human language. the AI have to detect wether people around are talking french or english during project time.

<hr>

<details><summary>Table of content</summary>

- [ALGOSUP_2022_Project_5_F](#algosup_2022_project_5_f)
  - [1. How does our AI works ?](#1-how-does-our-ai-works-)
  - [2. What do we use ?](#2-what-do-we-use-)
  - [3. Usage](#3-usage)
  - [4. Test if the model is working](#4-test-if-the-model-is-working)
  - [5. Deployment of the project](#5-deployment-of-the-project)
  - [6. Possible improvements](#6-possible-improvements)

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
You can display directly on the raspberry or on another computer connected to the same network.

## 3. Usage

How to setup the projects ?

If you want to recreate the project you must configure it with the following parameters:

execute the file `setup.sh` in order to create the directories used for boths of the datasets, the training, the testing and also to install the modules used to run the project.

after you need to install the [datasets](https://commonvoice.mozilla.org/en/datasets)

You can also put the datasets on google drive and use these datas if you link it with the following parameters:

```py
from google.colab import drive
drive.mount('/content/gdrive')
```

put them inside the respective directories. and execute all the cells of the notebook to prepare the datas, train the model, test the model and finally display the results.

You have 2 options to train the model:

- You can train the model with inceptionV3 which is a very powerful model with a very good accuracy(97.4%) but it will takes a lot of time to train and the .h5 file will be very big(about 130mb for us).
- Or you can train the model with a simpler model which will be faster to train but it will also have a lower accuracy(80.2%) and the .h5 file will be smaller(about 310kb for us).
  
## 4. Test if the model is working

In the directory [batch](./interface/predict/batch/) you have 2 .wav files, one in english and the other one in french that you can use to test the model.

you can use the following command to test the model with the samples:

```sh
python3 predict.py ./batch/english.wav ./batch/french.wav
```

## 5. Deployment of the project

We have chosen to deploy the project on a Raspberry PI 4 model B in order to have the best possible performance.

To display the result to the user we have setup a web server with Apache and a simple webpage to display the results.

To setup Apache, you have to install the following package:

```sh
sudo apt-get install apache2 -y
```

then you have to check if the server can be started with the following command:

```sh
hostname -I
```

To display the prediction of your model in real time, you have to install the following package:
you need to copy the directory [interface](./interface/) in the directory `/var/www/html/` of the Raspberry PI.

Finally, to access to the webpage you need to type the I.P address of your device in your browser.

## 6. Possible improvements

What we can do to improve the project?

- We can try to identify more languages.
- Make a phone application.
- Make the code to run it on an arduino.
- Setup a dockerfile to be able to run the project way more easily.
