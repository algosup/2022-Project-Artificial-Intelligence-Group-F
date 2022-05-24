# Functional specification

<hr>

<details><summary>Table of content</summary>

- [Functional specification](#functional-specification)
  - [1. Project scope](#1-project-scope)
    - [a. Goal](#a-goal)
    - [b. Deadlines](#b-deadlines)
  - [2. Privacy security](#2-privacy-security)
  - [3. Project specifications](#3-project-specifications)
    - [a. Hardware](#a-hardware)
    - [b. Software](#b-software)
      - [1. AI Training side](#1-ai-training-side)
</details>

<hr>

## 1. Project scope

### a. Goal

The goal of this project is to create an artificial intelligence capable of understanding when people are talking in french or in english and alert with a signal (a sound for exemple) when someone is talking in french during project time.

### b. Deadlines

The project will end the 27<sup>th</sup> June 2022.


## 2. Privacy security

We want to secure data collected by hardware's microphone, to be sure students discussions won't be leaked by any mean we won't save any data, once the AI identified the language spoken by students, it will automatically destroy any trace of the audio analysed.
Secondly, even if the device got hacked and someone manage to record conversations of students, the device won't be connected to internet and will work on a standalone.

## 3. Project specifications

  ### a. Hardware

This project include a device in addition of the software. 
We highly suggest an **Arduino Nano 33** as it's one of the smallest device that include a microphone.
But since this device have a small amount of storage and memory, we are not close to other device that could handle the project.

<img src="https://www.gotronic.fr/ori-carte-arduino-nano-33-ble-abx00034-30756.jpg" style='width:30vw'>

[Link to Arduino Store](https://store.arduino.cc/products/arduino-nano-33-ble)

  ### b. Software

In fact this project need 2 separate software, one to train the AI and another one to live host the AI offline.
It include the devellopment of a neural network that need to be trained on a device and used on another device.

  #### 1. AI Training side

A training side of an AI need a lot of computer power that means we can't use either the Arduino device as a training hardware. 
For it to be relevant, the training hardware need at least a GPU ( Graphic Processing Unit ) in order to process all the data at a good speed. 
We suggest the use of one of these website, that provide a GPU for free ( Limited time ):
| [Google Collab](https://colab.research.google.com/)  | [Kaggle](https://www.kaggle.com/) | 
| :--------------------------------------------------: | :-------------------------------: |

***

Both use the technology 'Jupiter Notebook' and Python3. Also they both allow Shell commands used to send command directly to the system.

***

For Neural network software there is currently 2 technologies that are currently viable for a Neural Network.

| [TensorFlow](https://www.tensorflow.org/)  | [PyTorch](https://pytorch.org/) | 
| :----------------------------------------: | :-----------------------------: |

TensorFlow is made by Google while PyTorch is made by Facebook. 

Both are different but end up in the same result.