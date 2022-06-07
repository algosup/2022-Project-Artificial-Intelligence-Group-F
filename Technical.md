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


### c. Convention of typing

We want to keep things easay so Snake case will be used everywhere.

## 4. Data

### a. Dataset

In order to train the AI, we need to have a dataset.
We don't have enough ressources and divercity in order to create our own dataset.
Mozilla 

### b. Converting dataset
### c. Retrieve Live data
