# Web VPython 3.2 – Pendulum Simulation (GlowScript)

A **3D interactive pendulum simulation** built using **GlowScript VPython**. This project visualizes a simple pendulum’s motion and its **kinetic, potential, and total energy** in real-time directly in your browser.

## 🔹 Features

* Real-time **3D visualization** of a pendulum.
* Dynamic **energy calculations** (Kinetic, Potential, and Total Energy).
* Displays **time period** (small-angle approximation) and **elapsed time**.
* **Trail** effect for the bob to visualize motion path.
* Adjustable **initial angle**, **bob mass**, and **string length** via user input.
* No installation required – works in any modern browser.

## 🔹 How to Run

1. Open [**GlowScript.org**](https://www.glowscript.org/).
2. Create a free account (optional, but recommended to save your code).
3. Click **“New Program”** → choose **VPython**.
4. Copy and paste the contents of `pendulum.py` (or your `.vpy` file) into the editor.
5. Click **Run** – the simulation will appear in your browser.

## 🔹 User Inputs

When the simulation runs, you will be prompted to enter:

* **Angle of suspension** (in degrees)
* **Mass of the bob** (in kg)
* **Length of the string** (in meters)

The pendulum will start swinging based on your inputs.

## 🔹 Physics Behind the Simulation

* The pendulum follows the **equation of motion**
* **Angular velocity** (`ω`) and **angle** (`θ`) are updated using the **Euler method**.
* **Kinetic energy**: ( KE = (1/2)*mv^2 )
* **Potential energy**: ( PE = m g h )
* **Total energy**: ( TE = KE + PE )

## 🔹 Dependencies

* Runs entirely in the browser using **GlowScript VPython**. No additional libraries required.

## 🔹 Screenshots
  <img width="1339" height="610" alt="image" src="https://github.com/user-attachments/assets/3222e83f-9bae-4dd5-a494-cf2df84be7e1" />

