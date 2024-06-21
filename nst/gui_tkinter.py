import os
import numpy as np
from PIL import Image, ImageTk
from argparse import ArgumentParser
from stylize import stylize  # Assuming this is where the stylize function is defined
import datetime  # Importing the datetime module
import tkinter as tk
from tkinter import filedialog

CONTENT_WEIGHT = 5e0
STYLE_WEIGHT = 5e2
TV_WEIGHT = 1e2
STYLE_LAYER_WEIGHT_EXP = 1
LEARNING_RATE = 1e1
BETA1 = 0.9
BETA2 = 0.999
EPSILON = 1e-08
VGG_PATH = "./Major Project - Neuro Style and Recognition/nst/imagenet-vgg-verydeep-19.mat"
POOLING = "max"

def build_parser():
    parser = ArgumentParser()
    parser.add_argument("--content", required=True, help="Content image")
    parser.add_argument("--styles", nargs="+", required=True, help="Style images")
    # Removed output argument
    parser.add_argument("--iterations", type=int, default=1000, help="Number of iterations")
    parser.add_argument("--content-weight", type=float, default=CONTENT_WEIGHT, help="Content weight")
    parser.add_argument("--style-weight", type=float, default=STYLE_WEIGHT, help="Style weight")
    parser.add_argument("--style-layer-weight-exp", type=float, default=STYLE_LAYER_WEIGHT_EXP, help="Style layer weight exponent")
    parser.add_argument("--tv-weight", type=float, default=TV_WEIGHT, help="Total variation regularization weight")
    parser.add_argument("--learning-rate", type=float, default=LEARNING_RATE, help="Learning rate")
    parser.add_argument("--beta1", type=float, default=BETA1, help="Adam: beta1 parameter")
    parser.add_argument("--beta2", type=float, default=BETA2, help="Adam: beta2 parameter")
    parser.add_argument("--epsilon", type=float, default=EPSILON, help="Adam: epsilon parameter")
    parser.add_argument("--network", default=VGG_PATH, help="Path to network parameters")
    parser.add_argument("--pooling", default=POOLING, help="Pooling layer configuration")
    parser.add_argument("--overwrite", action="store_true", help="Write file even if it exists")
    return parser

def run_neural_style_transfer(content_path, style_paths, iterations=1000, content_weight=CONTENT_WEIGHT, 
                              style_weight=STYLE_WEIGHT, style_layer_weight_exp=STYLE_LAYER_WEIGHT_EXP, 
                              tv_weight=TV_WEIGHT, learning_rate=LEARNING_RATE, beta1=BETA1, beta2=BETA2, 
                              epsilon=EPSILON, network=VGG_PATH, pooling=POOLING):
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

    content_image = imread(content_path)
    style_images = [imread(style) for style in style_paths]

    style_blend_weights = [1.0 / len(style_images) for _ in style_images]  # Equal weights for simplicity

    # Removed initial handling

    initial = None
    initial_noiseblend = 0.0  # Setting initial noise blend to 0.0 by default
    preserve_colors = False
    content_weight_blend = 1

    loss_arrs = None
    for iteration, image, loss_vals in stylize(
        network=network,
        initial=initial,
        initial_noiseblend=initial_noiseblend,
        content=content_image,
        styles=style_images,
        preserve_colors=preserve_colors,
        content_weight_blend=content_weight_blend,
        style_blend_weights=style_blend_weights,
        iterations=iterations,
        content_weight=content_weight,
        style_weight=style_weight,
        style_layer_weight_exp=style_layer_weight_exp,
        tv_weight=tv_weight,
        learning_rate=learning_rate,
        beta1=beta1,
        beta2=beta2,
        epsilon=epsilon,
        pooling=pooling,
    ):
        pass
    
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Construct the output file name with date and time
    output_file = "./Major Project - Neuro Style and Recognition/nst/results/Neuro-Style_" + current_datetime.strftime("%Y-%m-%d_%H-%M-%S") + ".jpg"
    # Save the image
    imsave(output_file, image)

def imread(path):
    img = np.array(Image.open(path)).astype(np.float32)
    return img

def imsave(path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    Image.fromarray(img).save(path, quality=95)

def select_content_image():
    path = filedialog.askopenfilename()
    if path:
        content_entry.delete(0, tk.END)
        content_entry.insert(0, path)
        display_image(content_image_frame, path)

def select_style_images():
    paths = filedialog.askopenfilenames()
    if paths:
        style_entry.delete(0, tk.END)
        style_entry.insert(0, ", ".join(paths))
        for path in paths:
            display_image(style_image_frame, path)

def display_image(frame, path):
    img = Image.open(path)
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(frame, image=img)
    panel.image = img
    panel.pack()

def start_neural_style_transfer():
    content_path = content_entry.get()
    style_paths = style_entry.get().split(", ")
    run_neural_style_transfer(content_path, style_paths)

# Create Tkinter GUI
root = tk.Tk()
root.title("Neural Style Transfer")

content_frame = tk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True)

content_label = tk.Label(content_frame, text="Content Image:")
content_label.pack(side=tk.LEFT)
content_entry = tk.Entry(content_frame)
content_entry.pack(side=tk.LEFT, padx=5)
content_button = tk.Button(content_frame, text="Browse", command=select_content_image)
content_button.pack(side=tk.LEFT)

style_frame = tk.Frame(root)
style_frame.pack(fill=tk.BOTH, expand=True)

style_label = tk.Label(style_frame, text="Style Images:")
style_label.pack(side=tk.LEFT)
style_entry = tk.Entry(style_frame)
style_entry.pack(side=tk.LEFT, padx=5)
style_button = tk.Button(style_frame, text="Browse", command=select_style_images)
style_button.pack(side=tk.LEFT)

start_button = tk.Button(root, text="Start Neural Style Transfer", command=start_neural_style_transfer)
start_button.pack()

# Frames to display selected images
content_image_frame = tk.Frame(root)
content_image_frame.pack(fill=tk.BOTH, expand=True)

style_image_frame = tk.Frame(root)
style_image_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
