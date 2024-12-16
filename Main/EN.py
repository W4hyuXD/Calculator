#!/usr/bin/env python3
# Kalkulator Dengan Python
# Coded by WahyuDin Ambia
# Update 16 Dec 2024
import os
from rich.panel import Panel as nel
from rich import print as cetak

# Warna
P2 = "[#FFFFFF]"
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
B2 = "[#00FFFF]"
H = "\x1b[38;5;46m"  # Hijau
ttk = f"{M2}● {K2}● {H2}●"

# Variabel Global Riwayat
riwayat_perhitungan = []

# Banner
def banner():
    os.system('clear')
    bener = f"""{ttk}
{P2}   [bold]_________      ________________               
    __  ____/_____ ___  /_  /___  /______________ 
    _  /    _  __ `/_  /_  __/_  __ \  __ \_  __ \+
    / /___  / /_/ /_  / / /_ _  / / / /_/ /  / / /
    \____/  \__,_/ /_/  \__/ /_/ /_/\____//_/ /_/ 
{M2}  ------------------------------------------------
{P2}  Calthon: Simple Calculator in Python
{P2}  Copyright © 2024 WahyuXD | Releases:{H2} 4 May 2024
{M2}  ------------------------------------------------
    """
    cetak(nel(bener, width=60, style='#ff0000'))

# riwayat
def tampilkan_riwayat():
    if riwayat_perhitungan:
        cetak(nel(f'{P2}Calculation History:\n\n' + '\n'.join(riwayat_perhitungan), title=f'{M2}( {P2}History{M2} )', style='#ff0000', width=50));exit()
    else:
        cetak(nel(f'{P2}No calculations yet.', title=f'{M2}( {P2}History{M2} )', style='#ff0000', width=50))

# kalkulator
def kalkulator():
    while True:
        banner()
        try:
            # opsi operasi
            cetak(nel(f'{P2}   What operation would you like to perform?', subtitle=f'{P2}╭─', subtitle_align='left', width=50, style='#ff0000'))
            oper = input(f'   ╰─(+,-,/,x):{H} ')
            print('')
            cetak(nel(f'{P2}             Enter the First Number', subtitle=f'{P2}╭─', subtitle_align='left', width=50, style='#ff0000'))
            x = float(input(f'   ╰─>{H} '))
            cetak(nel(f'{P2}              Enter the Second Number', subtitle=f'{P2}╭─', subtitle_align='left', width=50, style='#ff0000'))
            z = float(input(f'   ╰─>{H} '))
            print('')
            # Operasi hitung
            if oper == 'x':
                r = x * z
                operasi = "Multiplication"
            elif oper == '-':
                r = x - z
                operasi = "Subtraction"
            elif oper == '+':
                r = x + z
                operasi = "Addition"
            elif oper == '/':
                if z == 0:
                    raise ZeroDivisionError
                r = x / z
                operasi = "Division"
            else:
                cetak(f'\n{P2} [{M2}!{P2}] Invalid operation.')
                continue
            # simpan hasil ke riwayat
            hasil_str = f'Result of {operasi}: {x} {oper} {z} = {r:.2f}'
            riwayat_perhitungan.append(f'{P2}{hasil_str}')
            # Tampilkan hasil
            cetak(nel.fit(f'[white]{hasil_str}', title=f'( {P2}Result{M2} )', style='#ff0000'))

        except ZeroDivisionError:
            cetak(f'\n{P2} [{M2}!{P2}] Error: Cannot divide by zero.')
        except ValueError:
            cetak(f'\n{P2} [{M2}!{P2}] Invalid input, please enter valid numbers.')
        except Exception as e:
            cetak(f'\n{P2} [{M2}!{P2}] Unknown error: {e}')
  
        cetak(nel(f'{P2}Do you want to calculate again?', subtitle=f'{P2}╭─', subtitle_align='left', width=50, style='#ff0000'))
        ulang = input(f'   ╰─(y/n/r for history):{H} ').lower()
        if ulang == 'n':
            cetak(f'\n{P2} Thank you for using Calthon!')
            break
        elif ulang == 'r':
            tampilkan_riwayat()

if __name__ == '__main__':
    kalkulator()