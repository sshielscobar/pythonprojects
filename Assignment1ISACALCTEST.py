import math
import time 
import sys

#menu at the beginning
print(" ISA Calculator\n")

while True:
    user_input = input("For Meters, Press 1\nFor Feet, Press 2\nFor Flight Level, Press 3\n")

    if user_input == "1":
        alt = float(input("Enter Altitude [m]: "))
        break
    elif user_input == "2":
        alt = float(input("Enter Altitude [ft]: ")) / 3.28
        break
    elif user_input == "3":
        alt = float(input("Enter Altitude [FL]: ")) * 100 / 3.28
        break
    else:
        print("Invalid option. Please input one of the provided options.\n")

#constants no matter what
R = 287.05      
g = 9.81        
#calculating layer base values
#troposphere
T0 = 288.15     
P0 = 101325            
rho0 = 1.225 
L_tropo = -0.0065 
#tropopause
T1 = 216.65
P1 = 22632.1
#stratosphere lower layer
T2 = 216.65
P2 = 5474.89
L_strato = 0.001
#stratosphere upper layer
T3 = 228.65
P3 = 868.02
L_strato2 = 0.0028
#stratopause
T4 = 270.65
P4 = 110.91
#mesosphere lower layer
T5 = 270.65
P5 = 66.94
L_mesos0 = -0.0028
#mesosphere upper layer
T6 = 214.65
P6 = 3.956
L_mesos1 = -0.0020

#troposphere
if 0 < alt <= 11000:

    T = T0 + (L_tropo * alt)
    P = P0 * (T / T0) ** (-g / (L_tropo * R))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

#tropopause
elif alt <= 20000:
    
    T = T1
    P = P1 * math.exp(-g * (alt - 11000) / (R * T1))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

#stratosphere
elif alt <= 32000:

    T = T2 + (L_strato * (alt - 20000))
    P = P2 * (T / T2) ** (-g / (L_strato * R))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

#stratosphere
elif alt <= 47000:

    T = T3 + (L_strato2 * (alt - 32000))
    P = P3 * (T / T3) ** (-g / (L_strato2 * R))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

#stratopause
elif alt <= 51000:

    T = T4
    P = P4 * math.exp(-g * (alt - 47000) / (R * T4))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

#mesosphere first layer
elif alt <= 71000:

    T = T5 + (L_mesos0 * (alt - 51000))
    P = P5 * (T / T5) ** (-g / (L_mesos0 * R))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

#mesosphere second layer
elif alt <= 86000:
    T = T6 + (L_mesos1 * (alt - 71000))
    P = P6 * (T / T6) ** (-g / (L_mesos1 * R))
    rho = P / (R * T)

    t_percent = (T / T0) * 100
    p_percent = (P / P0) * 100
    rho_percent = (rho / rho0) * 100

else: 
    print("Value is not within ISA atmosphere. Shutting Down.")
    time.sleep(0.45)
    print(".") 
    time.sleep(0.45)
    print(".") 
    time.sleep(0.45)
    print(".") 
    sys.exit()

print("Calculating Values")
time.sleep(0.25)
print(".")
time.sleep(0.25)
print(".")
print(".\n", end="\r", flush=True)
time.sleep(0.1)

#FINAL OUTPUT TABLE W/ HUMAN-LIKE DELAY

def type_out(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

    # Type out header and altitude
type_out(f"\n Altitude: {alt:.0f} m", delay=0.03)
type_out("────────────────────────────────────────────", delay=0.002)
time.sleep(0.5)

# Table headers
type_out(f"{'Quantity':<15}{'Value':>15}    {'% of Sea Level':>20}", delay=0.01)
type_out("────────────────────────────────────────────", delay=0.002)
time.sleep(0.3)

# Type each row
type_out(f"{'Temperature (K)':<15}{T:>15.2f}    {t_percent:>20.2f}%", delay=0.005)
type_out(f"{'Pressure (Pa)':<15}{P:>15.2f}    {p_percent:>20.2f}%", delay=0.005)
type_out(f"{'Density (kg/m³)':<15}{rho:>15.4f}    {rho_percent:>20.2f}%", delay=0.005)

type_out("────────────────────────────────────────────", delay=0.002)