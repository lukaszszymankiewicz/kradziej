import tkinter as tk

from kradziej import get_scores_from_url


def succes_window():
    window = tk.Toplevel()

    label = tk.Label(window, text="Ukradnięte!")
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')


def failure_window(error):
    window = tk.Toplevel()

    label = tk.Label(window, text=error.args[0])
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')


def run_kradziej():
    url = globals()["entry"].get()
    try:
        get_scores_from_url(url)
    except Exception as error:
        failure_window(error)
    else:
        succes_window()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Kradziej nut wersja 1.0")
    root.geometry("500x300")

    label = tk.Label(
        text="wpisz url nutek do ukradniecia",
        width=30,
        height=5,
    )
    label.pack()

    entry = tk.Entry(
        width=200,
    )
    url = entry.get()
    entry.pack()

    stealing_button = tk.Button(
        name="stealing_button",
        text="Kradnij nutki!",
        width=25,
        height=5,
        command=run_kradziej,
    )
    stealing_button.pack()

    root.mainloop()

