import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from pyzbar import pyzbar


# browsing the image

def browse_image():
  filename=filedialog.askopenfilename(initialdir="/",title="Select a File",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
  if filename:
    show_image(filename)


def show_image(filename):
  global img_filename
  img_filename=filename
  qr_image=cv2.imread(filename)
  rgb_image=cv2.cvtColor(qr_image,cv2.COLOR_BGR2RGB)
  pil_image=Image.fromarray(rgb_image)
  img=ImageTk.PhotoImage(pil_image)
  image_label.config(image=img)
  image_label.image = img

#extracting the image

def extract_qr_data():
  if img_filename:
    qr_image = cv2.imread(img_filename)
    gray_image = cv2.cvtColor(qr_image, cv2.COLOR_BGR2GRAY)
    qrcodes = pyzbar.decode(gray_image)
    if qrcodes:
        qr_data = qrcodes[0].data.decode("utf-8")
        
        if qrcodes:
        # Extract data from the QR code
          qr_data = qrcodes[0].data.decode("utf-8")
        # Display the extracted data
          result_text.delete(1.0, tk.END)
          result_text.insert(tk.END, "QR Code Data: " + qr_data)
        else:
          result_text.delete(1.0, tk.END)
          result_text.insert(tk.END, "No QR code found in the image.")
  else:
      result_text.delete(1.0, tk.END)
      result_text.insert(tk.END, "Please select a QR code image first.")




root=tk.Tk()
root.title("QR Code Reader")
root.geometry("500x500")


# creating the interface


                            ##INTERFACE###



# Create Label for Title
label_title = tk.Label(root, text="QR Code Extractor", fg="White", bg="Navy Blue")
label_title.grid(row=0, column=0, columnspan=3, pady=5)
label_title.config(font=("Helvetica", 25, "bold"))

# Create Label for button
label_title = tk.Label(root, text="Upload QR Code Image", fg="Dark blue")
label_title.grid(row=1, column=0, columnspan=3, pady=5) 
label_title.config(font=("Helvetica", 10, "bold"))

# Initialize global variable for storing filename
img_filename = None

# Create button to browse QR code image
browse_image_button = tk.Button(root, text="Browse", command=browse_image)
browse_image_button.grid(row=2, column=0, columnspan=3)

# Create label to display image
image_label = tk.Label(root)
image_label.grid(row=3, column=0, columnspan=3)

# Create button to extract data
extract_data_button = tk.Button(root, text="Extract Data", command=extract_qr_data)
extract_data_button.grid(row=4, column=0)

# Create text widget to display extracted data
result_text = tk.Text(root, height=5, width=50)
result_text.grid(row=5, column=0, pady=10)

root.mainloop()
