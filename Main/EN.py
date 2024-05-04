#! usr/bin/env python3
# Kalkulator With Python 
# Tools Kalkulator Sederhana | © WahyuDin Ambia

# import module
import os, rich
from rich.panel import Panel as nel
from rich import print as cetak

# color
P2 = "[#FFFFFF]"
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
B2 = "[#00FFFF]"
H = "\x1b[38;5;46m"  # Hijau
ttk =f"{M2}● {K2}● {H2}●"

# banner
def banner():
    os.system('clear')
    cetak(nel(f'{ttk}\n\n\n         {P2}SIMPLE CALCULATOR IN  {B2}PYTHON{P2}\n\n              [on #ff0000][italic]Coded by WahyuXD.\n\n',width=50,title=f'( {P2}Banner{M2} )',style='#ff0000'))

# calculator
def kalkulator():
    banner()
    cetak(nel(f'{P2}What calculation operations do you want to use?',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
    oper = input(f'   ╰─(+,-,/,x):{H} ')
    print('')
    
    # perkalian
    if oper in ['x']:
        cetak(nel(f'{P2}If you use the count operation {H2}Multiplication{P2},\nplease enter the number you want {H2}multiply.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Enter the first number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}            Enter the second number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) * int(z)
        print('')
        cetak(nel.fit('[white]The result of Multiplication[green] {} [white]with[green] {}[white] is: [green]{}'.format(x,z,r),title=f'({P2} Result {M2})',style='#ff0000'))
        
    # pengurangan
    elif oper in ['-']:
        cetak(nel(f'{P2} If you use the count operation {H2}Subtraction{P2},\n please enter the number you want {H2}subtraction.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Enter the first number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}            Enter the second number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) - int(z)
        print('')
        cetak(nel.fit('[white]The result of Subtraction[green] {} [white]with[green] {}[white] is: [green]{}'.format(x,z,r),title=f'({P2} Result{M2} )',style='#ff0000'))
        
    # penjumlahan
    elif oper in ['+']:
        cetak(nel(f'{P2}  If you use the count operation {H2}Addition{P2},\n  please enter the number you want {H2}add up.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Enter the first number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}            Enter the second number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) + int(z)
        print('')
        cetak(nel.fit('[white]The result of Addition[green] {} [white]with[green] {}[white] is: [green]{}'.format(x,z,r),title=f'({P2} Result{M2} )',style='#ff0000'))
        
    # Pembagian
    elif oper in ['/']:
        cetak(nel(f'{P2}   If you use the count operation {H2}Division{P2},\n   please enter the number you want {H2}divide.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Enter the first number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}            Enter the second number',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) / int(z)
        print('')
        cetak(nel.fit('[white]The result of Division[green] {} [white]with[green] {}[white] is: [green]{}'.format(x,z,r),title=f'({P2} Result {M2})',style='#ff0000'))
    else:
        cetak(f'\n{P2} [{M2}!{P2}] Input Yang Bener Goblok.');exit()

if __name__=='__main__':
    kalkulator()
