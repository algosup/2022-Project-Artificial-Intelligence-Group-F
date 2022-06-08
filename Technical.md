# Technical specification

<hr>

<details><summary>Table of content</summary>

- [Technical specification](#technical-specification)
  - [1. Goal of the project](#1-goal-of-the-project)
  - [2. Hardware](#2-hardware)
    - [a. Main device](#a-main-device)
    - [b. Modules](#b-modules)
  - [3. Software](#3-software)
    - [a. Language](#a-language)
    - [b. Neural network](#b-neural-network)
    - [c. Convention of typing](#c-convention-of-typing)
  - [4. Data](#4-data)
    - [a. Dataset](#a-dataset)
    - [b. Converting dataset](#b-converting-dataset)
    - [c. Retrieve Live data](#c-retrieve-live-data)
</details>

<hr>

## 1. Goal of the project

Quick section as a reminder.
This project is designed to be able to detect if someone is talking in french or in english.
It have to he small enough to be hosted on a device such as a Raspberry Pi ar an Arduino.

This device won't need direct maintenance because it's not connected to internet.
But it can receive updates if we update the software manually.

## 2. Hardware

### a. Main device
This were first designed to be hosted on an Arduino Nano 33.
But since the Arduino Nano 33 is a small device, we decided to use a Raspberry Pi 4b.

The Raspberry Pi 4b is a powerful device that can be used to host the project.
It have 8Gb of RAM and the ability to have MicroSD card.

### b. Modules

Contrary to an Arduino Nano, the Raspberry Pi 4b doesn't have a microphone.
That way we need to add a module to the Raspberry Pi 4b to have a microphone.

This module is able to record audio and send it to the Raspberry Pi 4b.
It have more range than the Arduino Nano 33 (2 meters for the Module, 20cm for the Arduino).

It also have a better sound quality than the Arduino Nano 33.
It allow in the future to be able to push an update to voice recognition or vocal commands.



## 3. Software

### a. Language

We are going to use Python as a language to develop the project.
Python is a powerful, lightweight language for a Raspberry Pi.
It's also well supported by our Neural Network library.

### b. Neural network

We have a choice between using Tensorflow or Pytorch.
We decided to use Tensorflow because the people in the team are more used to Tensorflow.

We decided to use a CNN ( Convolutional Neural Network ) to detect the language.
Because CNN are more reliable than a simple RNN ( Recurrent Neural Network ) or a simple speech to text.

So we are just going to use a CNN of the spectrogram of the sound to detect the language.



### c. Convention of typing

We want to keep things easay so Snake case will be used everywhere.

## 4. Data

### a. Dataset

In order to train the AI, we need to have a dataset.
We don't have enough ressources and divercity in order to create our own dataset.
Mozilla give us the nessesary tools to create our own Dataset.

Mozilla have a crowd-sourced dataset that we can use. 
It's called the [Speech dataset](https://www.mozilla.org/en-US/speech-data/dataset/).


### b. Converting dataset

A CNN can't be used on a sound directly.
We need to convert the sound to a spectrogram.

In fact we need to convert each sound of the dataset to a spectrogram.

Here is a small example on how to convert a sound to a spectrogram.
```PYTHON
def spectrogram(sound):
    spectrogram = melspectrogram(sound)
    spectrogram = librosa.power_to_db(spectrogram)
    return spectrogram


for files in folder:
    sound = AudioSegment.from_file(files)
    sound.export("files.wav", format="wav")
    sound = AudioSegment.from_file("files.wav")
    sound_spectrogram = spectrogram(sound)
    sound_spectrogram.export("files.png", format="png")
```

### c. Retrieve Live data

For the live version of the project, we need to be able to retrieve the sound from the microphone.
The record will be saved temporarly in a file.

We will use our generated model to predict the language of the sound.
And finnaly we will delete the file. ( Security and Data protection )

```PYTHON	
def retrieve_live_data():
    sound = AudioSegment.from_microphone(channels=1, samplerate=16000, duration=5)
    sound.export("files.wav", format="wav")
    sound = AudioSegment.from_file("files.wav")
    sound_spectrogram = spectrogram(sound)
    sound_spectrogram.export("files.png", format="png")
    sound_spectrogram = Image.open("files.png")
    sound_spectrogram = np.array(sound_spectrogram)
    sound_spectrogram = sound_spectrogram.reshape(1, 1, sound_spectrogram.shape[0], sound_spectrogram.shape[1])
    prediction = model.predict(sound_spectrogram)
    os.remove("files.wav")
    os.remove("files.png")
    return prediction
```