import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class UploaFile:
    def __init__(self):
        self.root = None
        self.image_label=None
        self.status_label=None
        self.file_path=""
        self.accept_button=None

    def create_root(self):
        self.root = tk.Tk()
        self.root.minsize(300, 500)
        self.root.title("Upload Master Mind Image")

    def create_upload_dialogue(self):
        open_button = tk.Button(self.root, text="Open Image", command=self.open_file_dialog)
        open_button.pack(padx=20, pady=20)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(padx=25, pady=20)
        self.status_label = tk.Label(self.root, text="", padx=20, pady=10)

        self.status_label.pack()


        self.accept_button = tk.Button(self.root, text="Accept Image", command=self.accept_image_action)
        self.accept_button.pack_forget()

        self.root.mainloop()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])

        if file_path:
            self.file_path=file_path
            self.display_image(self.file_path)

        self.accept_button.pack()


    def display_image(self,file_path):
        image = Image.open(file_path)
        image1 = image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image1)
        self.image_label.config(image=photo)
        self.image_label.photo = photo
        self.status_label.config(text=f"Image loaded: {file_path}", wraplength =200)


    def accept_image_action(self):
        self.root.destroy()
        print("another thing")

    def main(self):
        self.create_root()
        self.create_upload_dialogue()
        return self.file_path


if __name__ == '__main__':

    dialogue_obj=UploaFile()
    dialogue_obj.main()
    print("first")
    print(dialogue_obj.file_path)
