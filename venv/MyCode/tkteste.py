import tkinter as tk

top = tk.Tk()
F = tk.Frame(top)
F.pack(fill="both")

fEntry = tk.Frame(F, border=1)
eHello = tk.Entry(fEntry)
eHello.pack(side="left")
lHistory = tk.Label(fEntry, text=" ", foreground="steelblue")
lHistory.pack(side="bottom", fill="x")
fEntry.pack(side="top")

def evClear():
    lHistory['text'] = eHello.get()
    eHello.delete(0, tk.END)

fButtons = tk.Frame(F, relief="sunken", border=1)
bClear = tk.Button(fButtons, text="Clear Text", command=evClear)
bClear.pack(side="left", padx=5, pady=2)
bQuit = tk.Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", padx=5, pady=2)
fButtons.pack(side="top", fill="x")

F.mainloop()
