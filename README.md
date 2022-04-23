# Welcome
MindMapper is an upcoming wearable meditational tool, that uses inbuilt sensors on the Micro:Bit to translate surroundings and user movements into audio.

This repository contains all the MaxMSP and Python scripts required for this project.

## MMinterfacing.py
This is the script that allows the Micro:Bit to send messages to the Max patch. It interprets when buttons are pressed or sensor values are changed, then converts them into a MIDI message to be transmitted. Below is a flowchart that outlines the functionality of this patch.

![A flow chart of the python file's signal flow](https://mindmappermeditate.files.wordpress.com/2022/04/pythonflow.png?w=466)

## MMGenerator.maxpat
This MaxMSP patch is responsible for the generation of all audio.
For an in depth description of the creation of this patch, see https://mindmappermeditate.wordpress.com/monthly-blog/

|  Sensor Input & Control # |  Purpose |
|---|---|
|21 – Accelerometer X	| Arpeggiator Direction
|22 – Accelerometer Y	| User control root note
|23 – Accelerometer Z	| User control arp notes
|24 – Compass Direction	| Pan arpeggiator
|25 – Magnetism Strength	| Binaural beat difference
|26 – Light Level	| Chord brightness
|27 – Temperature	| Master LPF
|31 – Button A	| User Contol / Fibbonacci
|32 – Button B	| Tempo
|33 – Button C	| Toggle Kick
|34 – Potentiometer	| Master Volume

## System Requirements
<ul>
  <li>MaxMSP 8 </li>
  <li>Mu Editor 1.1.0b7 </li>
  <li>MindMapper hardware, see https://mindmappermeditate.wordpress.com/how-to/ </li>
</ul>
