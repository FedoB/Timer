Simple Tkinter countdown timer.



To change the default time, change `TIME_START_DEF = "03:00"` on line 15.



You can press "spacebar" to play/pause the timer.

You can press "backspace" to change the background color.

You can press the checkmark on the top left to make the timer window "topmost" (it will get lifted over all other windows)

<img width="310" height="325" alt="image" src="https://github.com/user-attachments/assets/f939709c-2dc8-4dab-8979-a8c44940b8af" />

Troubleshooting:

\-It's a pyw file, opening it will immediately launch the program like an executable

\-If it doesn't start, you probably dont have pillow (PIL) installed. A simple `python -m pip install pillow` should solve your issues. Otherwise run the program from your terminal with `python Timer.pyw` and it will show you the error message.

