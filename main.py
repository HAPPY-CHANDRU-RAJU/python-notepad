import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFooter = Label(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Untitled file - Ctextpad")

        self.create_binding_keys()
        self.binding_functions_config()
        #icon
        self.new_image = tkinter.PhotoImage(file="new.png")
        self.open_image = tkinter.PhotoImage(file="open.png")
        self.save_image = tkinter.PhotoImage(file="save.png")
        self.exit_image = tkinter.PhotoImage(file="close.png")
        self.undo_image = tkinter.PhotoImage(file="undo.png")
        self.cut_image = tkinter.PhotoImage(file="cut.png")
        self.copy_image = tkinter.PhotoImage(file="copy.png")
        self.paste_image = tkinter.PhotoImage(file="paste.png")
        self.select_all_image = tkinter.PhotoImage(file="selectall.png")
        self.info_image = tkinter.PhotoImage(file="info.png")



        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W )
        self.__thisFooter.grid(sticky=S + W)

        # To open new file
        self.__thisFileMenu.add_command(label=" New", underline = 0, image = self.new_image,
                     compound = "left",command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label=" Open", underline = 0, image = self.open_image,
                     compound = "left",command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label=" Save", underline = 0, image = self.save_image,
                     compound = "left",command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label=" Exit", underline = 0, image = self.exit_image,
                     compound = "left",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label=" Undo", underline=0, image=self.undo_image,
                                        compound="left", command=self.__undo)

        self.__thisEditMenu.add_separator()
        self.__thisEditMenu.add_command(label=" Cut", underline = 0, image = self.cut_image,
                     compound = "left",command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label=" Copy", underline = 0, image = self.copy_image,
                     compound = "left",command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label=" Paste", underline = 0, image = self.paste_image,
                     compound = "left",command=self.__paste)

        self.__thisEditMenu.add_separator()

        self.__thisEditMenu.add_command(label=" Select All", underline=0, image=self.select_all_image,
                        compound="left", command=self.__SelectAll)
        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label=" About Notepad", underline = 0, image = self.info_image,
                     compound = "left",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

      #  self.__thisFooter.pack(side=BOTTOM, fill=Y)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    # exit()

    def __showAbout(self):
        showinfo("CtextPad", "Designed by : Chandru V")

    def __openFile(self, event=None):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - CTextPad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self, event=None):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self, event=None):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - CTextPad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
        return

    def __undo(self, event=None):
        self.__thisTextArea.event_generate("<<Undo>>")
        return

    def create_binding_keys(self):
        for key in ["<Control-a>", "<Control-A>"]:
            self.__thisTextArea.master.bind(key, self.__SelectAll)
        for key in ["<Control-z>", "<Control-Z>"]:
            self.__thisTextArea.master.bind(key, self.__undo)
        for key in ["<Control-n>", "<Control-N>"]:
            self.__thisTextArea.master.bind(key, self.__newFile)
        for key in ["<Control-S>", "<Control-s>"]:
            self.__thisTextArea.master.bind(key, self.__saveFile)
        for key in ["<Control-o>", "<Control-O>"]:
            self.__thisTextArea.master.bind(key, self.__openFile)

        return

    def binding_functions_config(self):
        self.__thisTextArea.tag_configure("sel", background="skyblue")
        self.__thisTextArea.configure(undo=True, autoseparators=True, maxundo=-1)
        return

    def __SelectAll(self, event=None):
        self.__thisTextArea.tag_add("sel", '1.0', 'end')
        return

    def lineCount(self,label):
        def repeater():
            page = self.__thisTextArea.get(1.0, END).split("\n")
            noLines = -1
            noLetters = 0
            for l in page:
                noLines +=1
                for w in l:
                    for c in w:
                        noLetters +=1
            label.config(text=str("Lines : {}, characters : {}".format(noLines,noLetters)), fg="black")
            label.after(1, repeater)
        repeater()

    def run(self):
        # Run main application
        self.lineCount(self.__thisFooter)
        self.__root.mainloop()


notepad = Notepad(width=800, height=600)
notepad.run()
