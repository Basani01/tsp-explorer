import tkinter as tk
from threading import Thread

class GUI:

    @staticmethod
    def showresults(Pdistance, AIdistance, declarewinner, pPath, aiPath):
        def run():
            resultscreen = tk.Tk()
            resultscreen.title("TSP Results")
            resultscreen.configure(bg="white")
            resultscreen.geometry("600x600")

            tk.Label(resultscreen, text="TSP Results", font=("Arial", 20, "bold"), bg="white").pack(pady=10)
            tk.Label(resultscreen, text=f"Player Total Distance: {Pdistance:.2f}", font=("Arial", 14), bg="white").pack(pady=5)
            tk.Label(resultscreen, text=f"AI Total Distance: {AIdistance:.2f}", font=("Arial", 14), bg="white").pack(pady=5)

            tk.Label(resultscreen, text=f"Winner: {declarewinner}", font=("Arial", 16, "bold"), fg="green", bg="white").pack(pady=10)

            # Player Path
            tk.Label(resultscreen, text="Player Path:", font=("Arial", 13, "bold"), bg="white").pack(pady=5)
            tk.Message(resultscreen, text=" → ".join(pPath), font=("Arial", 11), width=550, bg="#f0f0f0").pack(pady=5)

            # AI Path
            tk.Label(resultscreen, text="AI Path:", font=("Arial", 13, "bold"), bg="white").pack(pady=5)
            tk.Message(resultscreen, text=" → ".join(aiPath), font=("Arial", 11), width=550, bg="#f0f0f0").pack(pady=5)

            # Close button
            tk.Button(resultscreen, text="Close", command=resultscreen.destroy).pack(pady=20)

            resultscreen.mainloop()

        Thread(target=run).start()
