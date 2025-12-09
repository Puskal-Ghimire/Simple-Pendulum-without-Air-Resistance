Web VPython 3.2


# -----------------------------
# User Inputs
# -----------------------------
a = radians(float(input("Enter the angle of suspension of bob (degree): ")))
m = float(input("Enter the mass of bob (kg): "))
l = float(input("Enter the length of string (m): "))

# -----------------------------
# Setup Scene
# -----------------------------
hangingBar = box(pos=vector(0,0,0), size=vector(5,0.5,0.5), color=color.red)

bob = sphere(radius=0.2, color=color.red, make_trail=True, trail_color=color.green, retain=100,
             pos=vector(l*sin(a), -l*cos(a), 0))

rod = cylinder(pos=vector(0,0,0), axis=bob.pos - vector(0,0,0), radius=0.02, color=color.white)

# -----------------------------
# Physics Parameters
# -----------------------------
g = 9.8
omega = 0         # angular velocity
dt = 0.001        # time step
t_elapsed = 0

# -----------------------------
# Labels
# -----------------------------
ke_label = label(pos=vector(2,2,0), text="Kinetic Energy: 0 J", box=False)
pe_label = label(pos=vector(2,1.5,0), text="Potential Energy: 0 J", box=False)
te_label = label(pos=vector(2,1,0), text="Total Energy: 0 J", box=False)
period_label = label(pos=vector(2,0.5,0), text="", box=False)
elapsed_label = label(pos=vector(2,0,0), text="Elapsed Time: 0 s", box=False)

# Time period (small-angle approx)
T = 2*pi*sqrt(l/g)
period_label.text = f"Time Period: {T:.2f} s"


# -----------------------------
# Simulation Loop
# -----------------------------
while True:
    rate(1000)

    omega += -(g/l)*sin(a)*dt
    a += omega*dt

    # --- Update bob and rod positions ---
    bob.pos = vector(l*sin(a), -l*cos(a), 0)
    rod.axis = bob.pos - rod.pos

    # --- Energies ---
    v = omega*l
    KE = 0.5*m*v**2
    PE = m*g*(l - bob.pos.y)   # y=0 at pivot
    TE = KE + PE

    # --- Update labels ---
    ke_label.text = f"Kinetic Energy: {KE:.2f} J"
    pe_label.text = f"Potential Energy: {PE:.2f} J"
    te_label.text = f"Total Energy: {TE:.2f} J"

    # Update elapsed time
    t_elapsed += dt
    elapsed_label.text = f"Elapsed Time: {t_elapsed:.2f} s"
