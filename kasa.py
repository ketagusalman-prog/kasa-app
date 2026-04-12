import tkinter as tk

pairs = 6

def kaydet():
    print("\nKASA OTURMA PLANI\n")
    for i in range(pairs):
        sol = entries[i][0].get()
        sag = entries[i][1].get()
        print(f"Kasa {i+1}: {sol} | {sag}")

root = tk.Tk()
root.title("Kasa Oturma Plani")

entries = []

for i in range(pairs):
    tk.Label(root, text=f"Kasa {i+1}").grid(row=i, column=0)
    
    e1 = tk.Entry(root)
    e1.grid(row=i, column=1)
    
    e2 = tk.Entry(root)
    e2.grid(row=i, column=2)
    
    entries.append([e1, e2])

tk.Button(root, text="Kaydet", command=kaydet).grid(row=7, column=1)

root.mainloop()