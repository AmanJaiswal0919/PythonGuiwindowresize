from tkinter import*
 
root=Tk()
root.title("window resizer")
root.geometry("800x800")

def resize():
  w=width_entry.get()
  h=height_entry.get()

  root.geometry(f"{w}x{h}")

width=Label(root,text="width")
width.pack(pady=20)
width_entry=Entry(root)
width_entry.pack()

height=Label(root,text="height")
height.pack(pady=20)
height_entry=Entry(root)
height_entry.pack()

button=Button(root,text="resize",command=resize)
button.pack(pady=20)

root.mainloop()