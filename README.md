<h1>LCD display</h1>

<p>Liquid Crystal Display (LCD) is a type of alphanumeric or graphic display based on liquid crystals. LCDs are available in many different sizes, shapes and styles. In hackSpace we have the standard HD44780 LCD, which have 16 columns and 2 rows, for a total of 32 characters. The text is displayed on white and the background is blue. The single LED used in the display can be dimmed easily using a potentiometer or PWM, it uses less powered than LCD with EL (electroluminescent) backlight. These sorts of displays are used with machines or microcontrollers to measure data or distance of a specific component, however nowadays OLEDs are taking control of the market.</p>

<p>for getting the display to run using an arduino follow this guide on instructables</p>
<link>https://www.instructables.com/LCD-1602-With-Arduino-Uno-R3/</link>

<p>for using a rsapberry pi first install the following python dependencies in the terminal</p>

<p>sudo pip3 install serial GPIO time json requests</p>

<p>load the python file in this repository.</p>

<p>connect the LCD screen as shown in the diagram above.</p>

<p>We found that using GPIO pins for other purposes causes interference with the data pins on the LCD screen and in turn a garbled display. As a work around we used a serial connection form the raspberry pi to an arduino micro, then used this to manage all other digital inputs.</p>

<p>Load the arduino sketch attached to this document to the arduino micro. Connect the micro to the raspberry pi via USB.</p>

<p.Our example accesses a web API to generate a audio file. We used this web service... <link>https://api.sunoaiapi.com</link> many others are available.</p>
