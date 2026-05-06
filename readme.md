<h1>Simple Python countdown timer</h1>

<p align="center">
  <img width="310" height="325" alt="image" src="https://github.com/user-attachments/assets/f939709c-2dc8-4dab-8979-a8c44940b8af" />
</p>

To change the default time, change the mm:ss value on line 15: `TIME_START_DEF = "03:00"`.

You can press "spacebar" to play/pause the timer.

You can press "backspace" to change the background color.

You can press the checkmark on the top left to make the timer window stuck "topmost" (lifted over all other windows)

You can press the Play/Pause button (left) to play/pause the timer. When the timer is at zero, pressing it will start the timer to your previously set time.

You can press the Reset button (right) to reset the timer to your previusly set time, without starting the countdown.

After launching the program, or after pressing the Reset button, you may easily change the time by clicking the arrows above the mm:ss numbers.

<br>
Troubleshooting:

\-To download the file, go to "[Releases](https://github.com/FedoB/Timer/releases)" and download the file called: `Timer.pyw`

\-It's a pyw file, opening it will immediately launch the program like an executable

\-If it doesn't start, you probably dont have pillow (PIL) installed. A simple `python -m pip install pillow` should solve your issues. Otherwise run the program from your terminal with `python Timer.pyw` and it will show you the error message.

\-If you don't have Python installed, you can easily install it from the [Microsoft store](https://apps.microsoft.com/detail/9NQ7512CXL7T?hl=neutral&gl=IT&ocid=pdpshare).
