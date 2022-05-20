# ALGOSUP_2022_Project_5_F

The goal of this project is to create an AI to understand human language. the AI have to detect wether people around are talking french or english during project time.

<hr>

<details><summary>Table of content</summary>

- [1. What is an AI ?](#1-what-is-an-ai)
- [2. How does our AI works ?](#2-how-does-our-ai-works)
- [3. What do we use ?](#3-what-do-we-use)
- [4. Privacy security](#4-privacy-security)
</details>

<hr>

##  1. What is an AI ?

An Artificial Intelligence is a program wich can perform task where a certain level of intelgigence is required, for example to sort images, video or audio, an AI will search for precise patterns and then it will calculate probabilities and select the highest one to sort data.

##  2. How does our AI works ?

Firstly we had to import datasets, we currently have two datasets, one with english voices (70GB) and a second one with french voices (50GB).

Thanks to these datasets we can train or AI, to do that we are using [google colab](https://colab.research.google.com/?hl=en), it is a website where we can create ou AI in python and use Google's GPUs and CPUs to to train and test it with datasets before using it in real situation.

Then we transform audio files and recorded voices into a spectogram, it is a representation of sound in images. The AI can finally search for patterns inside theses images and sort languagues between french and english.

Our program will then send a signal if it detects french conversations.

##  3. What do we use ?

As said before we are using two [Datasets](https://drive.google.com/drive/folders/1SvLSIthSYgJJO5LWM9ecqLFiahR-dNqH?usp=sharing), one for english audio file and one for french audio files.

We are also using [Google colab](https://colab.research.google.com/?hl=en) for writing and traing our AI.

We are using an [Arduino nano 33 BLE](https://docs.arduino.cc/hardware/nano-33-ble) to store the AI and we are using its microphone to detect when someone is speaking

##  4. Privacy security

To guarantee conversation privacy, we choosed to delete every audio collected by our hardware after being analyzed by the AI to prevent possible leaks about user's conversation. 

Furthermore our hardware is not connected to any network, so the only way to connect to it is to use a USB cable.