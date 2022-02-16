import tkinter as tk
from imageFunc import *
from time import sleep

# Important Params:
desiredSize = (100, 70) # Change Later
def window():
    #img = cv2.imread("image.jpg")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    root = tk.Tk()
    root.geometry("1000x1000")
    T = tk.Text(root, height = 500, width = 500, font='TkFixedFont')
    T.pack()
    
    while True:
        ret, img = cap.read()

        width, height = img.shape[:2] # Original width and height
        output = cv2.resize(cv2.resize(img, (width * 2, height * 2)), desiredSize , interpolation=cv2.INTER_NEAREST)
        new_image = GetImageAverages(output)
        text = ''
        for i in new_image:
            for j in i:
                text += ASCII_PIXELS[int(j)]
            text += '\n'

        T.delete("1.0","end")
        T.insert(tk.END, text)
        

        root.update()
    

# def main(): 
    

if __name__ == "__main__":
    window()