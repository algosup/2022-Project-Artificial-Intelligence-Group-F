# ----------  Imports --------------
import numpy as np
import librosa
import os
import tensorflow as tf
import sounddevice as sd
from scipy.io.wavfile import write
from matplotlib import image as img
import json

# ----------  Values --------------

model = tf.keras.models.load_model("model.h5")

image_height = 128
image_width = 500

prob_french = None
prob_english = None
# ----------  Functions  --------------

def retrieve_live_data_and_save_as_png():
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    print("Recording...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # Record the sound
    sd.wait()  # Wait until recording is finished
    print("Saving...")
    write('output.wav', fs, myrecording)  # Save as WAV file

    y, sr = librosa.load('output.wav') # Load the audio file

    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128) # Create the spectrogram
    img.imsave('output.png', librosa.power_to_db(S, ref=np.max)) # Save the spectrogram as a PNG file
    return


def predict_live_sound():
    # Load the image

    img = tf.io.read_file("./output.png") # Read the image file
    tensor = tf.image.decode_png(img, channels=1) # Decode the image into a tensor
    tensor = tf.image.resize(tensor, [128, 500]) # Resize the image to the desired size

    input_tensor = tf.expand_dims(tensor, 0) # Create a batch of size 1, Or add a new dimension to the tensor that define the batch size
 

    # print('==========================================================')
    # print(input_tensor.shape)
    # print('==========================================================')

    input_tensor = tf.keras.applications.inception_v3.preprocess_input(input_tensor) # Preprocess the image to be compatible with the InceptionV3 model

    prediction = model(input_tensor) # Predict the class of the image

    test = prediction.numpy() # Convert the prediction to a numpy array

    #print(test[0][0]) # Print English probability
    #print(test[0][1]) # Print French probability

    prob_french = str(test[0][1]) # Save French probability
    prob_english = str(test[0][0]) # Save English probability

    data = { 
        "english": prob_english,
        "french": prob_french
    }
    json_string = json.dumps(data) # Convert the data to a json string
    with open('value.json', 'w') as outfile: # Write the json string to a file
        outfile.write(json_string)
    

    os.remove('output.wav') # Remove the audio file
    os.remove('output.png') # Remove the image file
    
    return


# ----------  MAIN --------------

while True:
    retrieve_live_data_and_save_as_png()
    predict_live_sound()






