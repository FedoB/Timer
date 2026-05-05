Simple Tkinter countdown timer.



To change the default time, change `TIME\_START\_DEF = "03:00"` on line 15.



You can press "spacebar" to play/pause the timer.

You can press "backspace" to change the background color.

You can press the checkmark on the top left to make the timer window "topmost" (it will get lifted over all other windows)



Troubleshooting:

\-It's a pyw file, so opening it will immediatly start the program like an execeutable

\-If it doesn't start, you probably dont have pillow (PIL) installed. A simple `python -m pip install pillow` should solve your issues. Otherwise run the program from your terminal with `python Timer.pyw` and it will show you the error message.

