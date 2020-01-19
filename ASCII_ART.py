from tkinter import filedialog
from tkinter import *
import PIL
from PIL import Image
import os, math

#creates a tkinter window and hides it
root = Tk()
root.title("Ascii Art Convertor")
root.withdraw()

#empty text variable
text = ""

#grayscale
grayscale = " .',;:clodxkO0KXNWM"

#selecting the image
image_fn = filedialog.askopenfilename(initialdir=".", title="Select File", filetypes =[("JPG Files", "*.jpg"), ("PNG Files", "*.png")])

#setting up the image
image = PIL.Image.open(image_fn)
image = image.convert('RGB')
factor = image.height / 300
image = image.resize((int(round(image.width / factor)), int(round(image.height / factor))))

#creates the text
for py in range(image.height):
    for px in range(image.width):
        b = sum(image.getpixel((px, py))) / 3
        char = grayscale[int((b*(len(grayscale) - 1))/255)]
        text += char
        text += " "
    text += "\n"

#save as
text_fn = filedialog.asksaveasfilename(defaultextension=".txt", filetypes =[("Text File", "*.txt")], confirmoverwrite=False)
print(text_fn)
f = open(text_fn, "w")
f.write(text)    
f.close()


    





 
