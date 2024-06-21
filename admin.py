import tkinter as tk
import ttkbootstrap as ttk
import subprocess
import threading
import os
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

#class for app window
class NeuralApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Neural App")

        # Calculate window dimensions
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = int(screen_width * 0.5) #680
        window_height = int(screen_height * 0.7) #537
        # print(window_height, window_width)

        # Set window size
        self.master.geometry(f"{window_width}x{window_height}")

        # Create a Notebook (multi-tabbed window)
        self.notebook = ttk.Notebook(self.master, bootstyle="dark")
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create and add tabs to the Notebook
        self.home_tab = ttk.Frame(self.notebook)
        self.neuro_rec_tab = ttk.Frame(self.notebook)
        self.neuro_tran_tab = ttk.Frame(self.notebook)
        self.gallery_tab = ttk.Frame(self.notebook)
        self.about_us_tab = ttk.Frame(self.notebook)


        self.notebook.add(self.home_tab, text="Home")
        self.notebook.add(self.neuro_rec_tab, text="Neuro-Recognition")
        self.notebook.add(self.neuro_tran_tab,text="Neuro-Transfer")
        self.notebook.add(self.gallery_tab, text="Gallery")
        self.notebook.add(self.about_us_tab, text="About Us")

#Creating widgets for various tabs
        self.create_home_widgets() # Create widgets for the Home tab
        self.create_neuro_rec_widgets() # Create widgets for the Recognition tab
        self.create_neuro_tran_widgets() # Create widgets for the NST tab
        self.create_gallery_widgets() # Create widgets for the Gallery tab
        self.create_about_us_widgets() # Create widgets for the About Us tab

#Creating Home Page 
    def create_home_widgets(self):
        # Heading
        heading_label = ttk.Label(self.home_tab, text="Neuro-Style & Recognition", font=("Helvetica", 20, "bold"))
        heading_label.pack(pady=25)

        # Label frame with text
        label_frame = ttk.LabelFrame(self.home_tab, text="What???")
        label_frame.pack(pady=0)
        # Configure font and size for the label frame text
        s = ttk.Style()
        s.configure('TLabelframe.Label', font=('Helvetica', 15, 'bold'))    

        info_label = ttk.Label(label_frame, text="Neural style transfer allows for the artistic transformation of images by adopting the stylistic elements of reference images, while digit recognition serves as a foundational task in neural network in which we first creates a model using MNIST and then trained a model that can recognize digits. The most important thing was to make all these work with the help of GUI.", wraplength=400)
        info_label.pack(padx=10, pady=10)
        # Configure font and size for the content text
        s = ttk.Style()
        s.configure('TLabel', font=('Helvetica', 7))
     
        # Buttons aligned in a line
        button_frame = ttk.Frame(self.home_tab)
        button_frame.pack()

        # Digit Recognition Tree View
        self.digit_recognition_tree = ttk.Treeview(button_frame)
        self.digit_recognition_tree.heading("#0", text="Digit Recognition")  # Set heading

        # Inserting top-level items
        self.digit_recognition_tree.insert("", "end", text="Research Paper")
        self.digit_recognition_tree.insert("", "end", text="Dataset")
        self.digit_recognition_tree.insert("", "end", text="Model Training")
        self.digit_recognition_tree.insert("", "end", text="UI")

        # Get the item ID of the "Dataset" item
        research_id = self.digit_recognition_tree.get_children()[0]
        dataset_id = self.digit_recognition_tree.get_children()[1]
        model_id = self.digit_recognition_tree.get_children()[2]
        ui_id = self.digit_recognition_tree.get_children()[3]

        # Insert "MNIST" under "Dataset"
        self.digit_recognition_tree.insert(research_id, "end", text="Geeks for Geeks")
        self.digit_recognition_tree.insert(research_id, "end", text="Researchgate.in")
        self.digit_recognition_tree.insert(dataset_id, "end", text="MNIST")
        self.digit_recognition_tree.insert(model_id, "end", text="Neural Network")
        self.digit_recognition_tree.insert(ui_id, "end", text="Gradio")

        # Packing the TreeView
        self.digit_recognition_tree.pack(side=tk.LEFT, padx=5, pady=10)

        # Neural Style Transfer Button
        self.digit_recognition_tree = ttk.Treeview(button_frame)
        self.digit_recognition_tree.heading("#0", text="Style Transfer")  # Set heading

        # Inserting top-level items
        self.digit_recognition_tree.insert("", "end", text="Research Paper")
        self.digit_recognition_tree.insert("", "end", text="Dataset")
        self.digit_recognition_tree.insert("", "end", text="Model Training")
        self.digit_recognition_tree.insert("", "end", text="UI")

        # Get the item ID of the "Dataset" item
        research_id = self.digit_recognition_tree.get_children()[0]
        dataset_id = self.digit_recognition_tree.get_children()[1]
        model_id = self.digit_recognition_tree.get_children()[2]
        ui_id = self.digit_recognition_tree.get_children()[3]

        # Insert "MNIST" under "Dataset"
        self.digit_recognition_tree.insert(research_id, "end", text="Tensorflow")
        self.digit_recognition_tree.insert(research_id, "end", text="Github")
        self.digit_recognition_tree.insert(dataset_id, "end", text="VGG 19")
        self.digit_recognition_tree.insert(model_id, "end", text="Neural Network")
        self.digit_recognition_tree.insert(ui_id, "end", text="Tkinter")

        # Packing the TreeView
        self.digit_recognition_tree.pack(side=tk.LEFT, padx=5, pady=10)

        # Centering button_frame within the Home tab
        button_frame.pack(expand=True)
        button_frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    #function to access files that need to be executed when clicked
    def run_digit_recognition(self):
        def run_command_dr():
            # Run the digit recognition script
            subprocess.run(["python", "./Major Project - Neuro Style and Recognition/digit/ui_gradio.py"])
            # Close the tkinter window
            self.master.destroy()
                    
        # Start a new thread to run the command
        command_thread = threading.Thread(target=run_command_dr)
        command_thread.start()
    def run_neural_style_transfer(self):
    # Define the function to run the command
        def run_command_nst():
            subprocess.run(["python", "./Major Project - Neuro Style and Recognition/nst/gui_tkinter.py"])
            # Close the tkinter window
            self.master.destroy()
        
        # Start a new thread to run the command
        command_thread = threading.Thread(target=run_command_nst)
        command_thread.start()
#Home page Over

#Creating Neuro-Recognition Page        
    def create_neuro_rec_widgets(self):
        # Heading
        heading_label = ttk.Label(self.neuro_rec_tab, text="Neuro-Digit Recognition", font=("Helvetica", 20, "bold"))
        heading_label.pack(pady=25)

        # Load the image
        image_path = "./Major Project - Neuro Style and Recognition/icons/mnist.jpeg"  # Replace with the actual path to your image
        image = Image.open(image_path)
        image = image.resize((275, 187))  # Adjust the size as necessary
        tk_image = ImageTk.PhotoImage(image)

        # Create a label for the image
        image_label = ttk.Label(self.neuro_rec_tab, image=tk_image)
        image_label.image = tk_image  # Keep a reference to avoid garbage collection
        image_label.pack(pady=0)

        # Label frame with text
        label_frame = ttk.LabelFrame(self.neuro_rec_tab, text="Digit Recognition")
        label_frame.pack(pady=10)

        info_label = ttk.Label(label_frame, text="Users can draw digits on a canvas provided within the application. Once the digit is drawn, the trained model embedded within the application will analyze the input and provide recognition of the digit drawn.\n   >> Model Train\n   >> Canvas Drawing \n   >> Model Recognition \n   >> Recognition Result", wraplength=400)
        info_label.pack(padx=10, pady=10)

        # Configure font and size for the label frame text
        s = ttk.Style()
        s.configure('TLabelframe.Label', font=('Helvetica', 15, 'bold'))
        # Configure font and size for the content text
        s.configure('TLabel', font=('Helvetica', 11))
        
        button = ttk.Button(self.neuro_rec_tab, text="Let's Try!!", command=self.run_digit_recognition)
        button.pack(side=tk.RIGHT, padx=(5, 10), pady=0)  # Place on the right side
        button.place(relx=0.793, rely=0.88, anchor=tk.NE)  # Place on the corner of the label frame
#Digit Recognition Page Over

#Creating Neuro-Style-Transfer Page        
    def create_neuro_tran_widgets(self):
        # Heading
        heading_label = ttk.Label(self.neuro_tran_tab, text="Neuro-Style Transfer", font=("Helvetica", 20, "bold"))
        heading_label.pack(pady=25)

        # Load the image
        image_path = "./Major Project - Neuro Style and Recognition/icons/nst.png"  # Replace with the actual path to your image
        image = Image.open(image_path)
        image = image.resize((275, 187))  # Adjust the size as necessary
        tk_image = ImageTk.PhotoImage(image)

        # Create a label for the image
        image_label = ttk.Label(self.neuro_tran_tab, image=tk_image)
        image_label.image = tk_image  # Keep a reference to avoid garbage collection
        image_label.pack(pady=0)

        # Label frame with text
        label_frame = ttk.LabelFrame(self.neuro_tran_tab, text="Style Transfer")
        label_frame.pack(pady=10)

        info_label = ttk.Label(label_frame, text="Neural style transfer is an optimization technique used to take two images, a content and a style reference image, and blend them so the output image looks like the content image, but “painted” in the style of the style reference image.\n   >> VGG-19\n   >> Stylize \n   >> Process implementor \n   >> UI", wraplength=400)
        info_label.pack(padx=10, pady=10)

        # Configure font and size for the label frame text
        s = ttk.Style()
        s.configure('TLabelframe.Label', font=('Helvetica', 15, 'bold'))
        # Configure font and size for the content text
        s.configure('TLabel', font=('Helvetica', 11))        
        button = ttk.Button(self.neuro_tran_tab, text="Let's Try!!", command=self.run_neural_style_transfer)
        button.pack(side=tk.RIGHT, padx=(5, 10), pady=0)  # Place on the right side
        button.place(relx=0.806, rely=0.88, anchor=tk.NE)  # Place on the corner of the label frame
#NST Page Over

#Creating Gallery Page        
    def create_gallery_widgets(self):
        # Heading
        heading_label = ttk.Label(self.gallery_tab, text="Gallery", font=("Helvetica", 20, "bold"))
        heading_label.pack(pady=25)

        # Create a Canvas widget for the gallery
        gallery_canvas = tk.Canvas(self.gallery_tab)
        gallery_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar for the gallery
        scrollbar = ttk.Scrollbar(self.gallery_tab, orient=tk.VERTICAL, command=gallery_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Canvas to use the Scrollbar
        gallery_canvas.configure(yscrollcommand=scrollbar.set)

        # Frame inside the Canvas to hold gallery items
        gallery_frame = tk.Frame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_frame, anchor=tk.NW)
        def show_image_popup(image_path):
            # Load the image
            image = Image.open(image_path)
            
            # Create a new window
            popup_window = tk.Toplevel()
            popup_window.title("Preview")
            
            # Display the image in a label
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(popup_window, image=photo)
            label.image = photo  # Keep a reference to prevent image from being garbage collected
            label.pack()
            
            # Function to close the popup window
            def close_popup():
                popup_window.destroy()
            
            # Button to close the popup window
            close_button = ttk.Button(popup_window, text="Close", command=close_popup)
            close_button.pack(pady=10)

        # Function to add gallery items (images)
        def add_gallery_item(path):
            # Check if the path is for an image
            if path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Load image
                image = Image.open(path)
                image.thumbnail((200, 200))  # Resize image
                photo = ImageTk.PhotoImage(image)
                # Create label to display image
                label = tk.Label(gallery_frame, image=photo)
                label.image = photo  # Keep a reference
                label.grid(row=add_gallery_item.row, column=add_gallery_item.col, padx=10, pady=10)
                # Add click event to show image popup
                label.bind("<Button-1>", lambda event, path=path: show_image_popup(path))
                # Update row and column indices
                add_gallery_item.col += 1
                if add_gallery_item.col >= 3:
                    add_gallery_item.col = 0
                    add_gallery_item.row += 1
            else:
                print("Unsupported file format:", path)
        
        # Initialize row and column indices
        add_gallery_item.row = 0
        add_gallery_item.col = 0
        
        # Path to your assets folder
        assets_folder = "./Major Project - Neuro Style and Recognition/nst/results"

        # Gather paths of image files
        image_paths = [os.path.join(assets_folder, file) for file in os.listdir(assets_folder) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        # Add gallery items
        for path in image_paths:
            add_gallery_item(path)

        # Update the gallery size when the frame is changed
        def on_frame_configure(event):
            gallery_canvas.configure(scrollregion=gallery_canvas.bbox("all"))

        gallery_frame.bind("<Configure>", on_frame_configure)        
#Gallery Page Over

#Creating About Us Page        
    def create_about_us_widgets(self):
        # Heading
        heading_label = ttk.Label(self.about_us_tab, text="About Us", font=("Helvetica", 20, "bold"))
        heading_label.pack(pady=25)

        # Frame to hold images and names
        image_frame = tk.Frame(self.about_us_tab)
        image_frame.pack(pady=0)

        # Load and display the first image with name
        image1_path = "./Major Project - Neuro Style and Recognition/icons/1.png"  # Replace with the path to your first image
        image1 = Image.open(image1_path)
        image1.thumbnail((150, 150))  # Resize image
        photo1 = ImageTk.PhotoImage(image1)
        label_image1 = tk.Label(image_frame, image=photo1)
        label_image1.image = photo1
        label_image1.grid(row=0, column=0, padx=5, pady=5)

        label_name1 = ttk.Label(image_frame, text="Shaury Shobit")
        label_name1.grid(row=1, column=0, padx=10, pady=5)

        # Load and display the second image with name
        image2_path = "./Major Project - Neuro Style and Recognition/icons/2.png"  # Replace with the path to your second image
        image2 = Image.open(image2_path)
        image2.thumbnail((150, 150))  # Resize image
        photo2 = ImageTk.PhotoImage(image2)
        label_image2 = tk.Label(image_frame, image=photo2)
        label_image2.image = photo2
        label_image2.grid(row=0, column=1, padx=5, pady=5)

        label_name2 = ttk.Label(image_frame, text="Pragya Yadav")
        label_name2.grid(row=1, column=1, padx=10, pady=5)

        # Label frame with text
        label_frame = ttk.LabelFrame(self.about_us_tab, text="About Us")
        label_frame.pack(pady=0)
        info_label = ttk.Label(label_frame, text="We are both MCA final-year students from batch 2022–2024 at Vivekananda Institute of Professional Studies.\nOur project is based on the knowledge we have gained from our MCA. We used our past experience working on Python-related projects to implement this project.\nImplementing any application with a simple user interface is the main objective.\n  >>Learn new topics\n  >>Implement our modules\n  >>Integrate with UI\n  >>Easy and simple UI", wraplength=500, font=("Helvetica", 10))
        info_label.pack(padx=10, pady=10)
#About Us Page Over
def main():
    root = tk.Tk()
    app = NeuralApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
