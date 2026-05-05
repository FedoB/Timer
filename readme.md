Simple Tkinter countdown timer.



To change the default time, change `TIME_START_DEF = "03:00"` on line 15.



You can press "spacebar" to play/pause the timer.

You can press "backspace" to change the background color.

You can press the checkmark on the top left to make the timer window stuck "topmost" (lifted over all other windows)

You can press the Play/Pause button (left) to play/pause the timer. When the timer is at zero, pressing it will start the timer to your previously set time.

You can press the Reset button (right) to reset the timer to your previusly set time, without starting the countdown.

After launching the program, or after pressing the Reset button, you may easily change the time by clicking the arrows above the mm:ss numbers.

<img width="310" height="325" alt="image" src="https://github.com/user-attachments/assets/f939709c-2dc8-4dab-8979-a8c44940b8af" />
\-
\-
Troubleshooting:

\-It's a pyw file, opening it will immediately launch the program like an executable

\-If it doesn't start, you probably dont have pillow (PIL) installed. A simple `python -m pip install pillow` should solve your issues. Otherwise run the program from your terminal with `python Timer.pyw` and it will show you the error message.

