# DataBorad
A Python projects which monitor the serial port connected to a computer (Windows) and visually display.

# Summary
At present, all features of the original version are developed and designed for Ms. Li's（CUMT） needs, and all of the features are available under the developer's（Yeah，only me just temporary）license. Of course, we also support the learning use and modification of this code, and hope that a more perfect version can be released. Thank you to everyone who has seen this software.

# About Code
## Now Progress

Release 1.0
At present, this program is mainly used to record and display the digital data received from the serial port, adopted Flask and Pyecharts to built the application.I tried to improve the stability of the program, but something was still missing **such as**：
- Hot swap of serial port devices.
- The incoming data is non-numeric.
- The serial port suddenly shuts down.
- Request fluctuation when just started.
- Disorder of timing（ Sporadically ）.
- etc...
As you can see, the current program is still a very unstable program, I hope that someone can continue to develop, together to complete a fucking special serial port reception and display program.
On how to use it, just run app.py (with the required library installed beforehand, of course).
**imports**
- flask & flask_apscheduler
- json
- pyecharts
- serial & serial.tools.list_ports
- re & csv & os & sys （yeah，These are libraries that the system already owns）

By the way,The whole design pattern is very flawed, which I discovered when I was almost done, and I wish I had time to refactor the entire code (hopefully I can do it soon).

# Last but not least
The code level is the same as SHIT, I hope you can forgive me (Just Please) :<

![OIP-C](https://user-images.githubusercontent.com/56034408/224262133-91e5303c-9fee-42b8-b258-fad439c8c712.jpg)

