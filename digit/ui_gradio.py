import gradio as gr
import tensorflow as tf
import numpy as np
import random

# Dictionary to store multiple fun facts for each digit
fun_facts = {
    '0': [
        "Fun fact 1 for digit 0.",
        "Fun fact 2 for digit 01.",
        "Fun fact 3 for digit 02.",
        "Fun fact 4 for digit 03.",
        "Fun fact 5 for digit 04."
    ],
    '1': [
        "Fun fact 1 for digit 1.",
        "Fun fact 2 for digit 12.",
        "Fun fact 3 for digit 13.",
        "Fun fact 4 for digit 14.",
        "Fun fact 5 for digit 15."
    ],
    '2': [
        "Fun fact 1 for digit 2.",
        "Fun fact 2 for digit 21.",
        "Fun fact 3 for digit 22.",
        "Fun fact 4 for digit 23.",
        "Fun fact 5 for digit 24."
    ],
    '3': [
        "Fun fact 1 for digit 3.",
        "Fun fact 2 for digit 3.",
        "Fun fact 3 for digit 3.",
        "Fun fact 4 for digit 3.",
        "Fun fact 5 for digit 3."
    ],
    '4': [
        "Fun fact 1 for digit 4.",
        "Fun fact 2 for digit 4.",
        "Fun fact 3 for digit 4.",
        "Fun fact 4 for digit 4.",
        "Fun fact 5 for digit 4."
    ],
    '5': [
        "Fun fact 1 for digit 5.",
        "Fun fact 2 for digit 5.",
        "Fun fact 3 for digit 5.",
        "Fun fact 4 for digit 5.",
        "Fun fact 5 for digit 5."
    ],
    '6': [
        "Fun fact 1 for digit 6.",
        "Fun fact 2 for digit 6.",
        "Fun fact 3 for digit 6.",
        "Fun fact 4 for digit 6.",
        "Fun fact 5 for digit 6."
    ],
    '7': [
        "Fun fact 1 for digit 7.",
        "Fun fact 2 for digit 7.",
        "Fun fact 3 for digit 7.",
        "Fun fact 4 for digit 7.",
        "Fun fact 5 for digit 7."
    ],
    '8': [
        "Fun fact 1 for digit 8.",
        "Fun fact 2 for digit 8.",
        "Fun fact 3 for digit 8.",
        "Fun fact 4 for digit 8.",
        "Fun fact 5 for digit 8."
    ],
    '9': [
        "Fun fact 1 for digit 9.",
        "Fun fact 2 for digit 9.",
        "Fun fact 3 for digit 9.",
        "Fun fact 4 for digit 9.",
        "Fun fact 5 for digit 9."
    ]
}

# Load the trained model
model = tf.keras.models.load_model('F:/Project/Major Project - Neuro Style and Recognition/digit/digit.h5')

# Function to fetch random fun fact based on predicted digit
def get_fun_fact(predicted_digit):
    return random.choice(fun_facts[predicted_digit])

# Function to recognize digit
def recognize_digit(image):
    if image is not None:
        image = image.reshape(1, 28, 28, 1).astype('float32') / 255
        prediction = model.predict(image)[0]
        top_predicted_digit = str(np.argmax(prediction))
        top_3_indices = np.argsort(prediction)[::-1][:3]
        top_3_probs = [float(prediction[i]) for i in top_3_indices]  # Convert NumPy float32 to Python float
        top_3_digits = [str(i) for i in top_3_indices]
        fun_fact = get_fun_fact(top_predicted_digit)
        return {digit: prob for digit, prob in zip(top_3_digits, top_3_probs)}, fun_fact
    else:
        return {}, ''

# Create a Gradio interface
iface = gr.Interface(
    fn=recognize_digit,
    inputs=gr.inputs.Image(shape=(28, 28), image_mode='L', invert_colors=True, source='canvas', label="Draw a digit"),
    outputs=[
        gr.outputs.Label(num_top_classes=3, label="Predicted Digit"),
        gr.outputs.Label(label="Fun Fact")
    ],
    theme="compact",
    title="Handwritten Digit Recognition",
    description="Draw a digit on the canvas and see the predicted digit along with a fun fact!",
    allow_flagging=False,
    live=True
)

iface.launch(share=True)
