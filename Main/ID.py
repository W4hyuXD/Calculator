#! usr/bin/env python3
# Kalkulator With Python 

import os, rich
from rich.tree import Tree as tri
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

def banner():
    os.system('clear')
    cetak(nel(f'{ttk}\n\n\n      {P2}KALKULATOR SEDERHANA DENGAN {B2}PYTHON{P2}\n\n              [on #ff0000][italic]Coded by WahyuXD.\n\n',width=50,title=f'( {P2}Banner{M2} )',style='#ff0000'))

def kalkulator():
    banner()
    cetak(nel(f'{P2}   Ingin Menggunakan Operasi Hitung Apa?',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
    oper = input(f'   ╰─(+,-,/,x):{H} ')
    print('')
    # perkalian
    if oper in ['x']:
        cetak(nel(f'{P2} Anda Menggunakan Operasi Hitung {H2}Perkalian{P2},\n Silahlan Masukkan Angka Yang Ingin Anda\n Kalikan.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Masukkan Angka Pertama',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}              Masukkan Angka Kedua',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) * int(z)
        print('')
        cetak(nel.fit('[white]Hasil Dari Perkalian [green]{} [white]Dengan[green] {}[white] Adalah: [green]{}'.format(x,z,r),title=f'({P2} Result {M2})',style='#ff0000'))
    # pengurangan
    elif oper in ['-']:
        cetak(nel(f'{P2} Anda Menggunakan Operasi Hitung {H2}Pengurangan{P2},\n Silahlan Masukkan Angka Yang Ingin Anda\n Kurangi.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}            Masukkan Angka Pertama',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}              Masukkan Angka Kedua',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) - int(z)
        print('')
        cetak(nel.fit('[white]Hasil Dari Pengurangan [green]{} [white]Dengan[green] {}[white] Adalah: [green]{}'.format(x,z,r),title=f'({P2} Result{M2} )',style='#ff0000'))
    # penjumlahan
    elif oper in ['+']:
        cetak(nel(f'{P2} Anda Menggunakan Operasi Hitung {H2}Penjumlahan{P2},\n Silahlan Masukkan Angka Yang Ingin Anda\n Jumlahkan.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Masukkan Angka Pertama',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}              Masukkan Angka Kedua',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) + int(z)
        print('')
        cetak(nel.fit('[white]Hasil Dari Penjumlahan [green]{} [white]Dengan[green] {}[white] Adalah: [green]{}'.format(x,z,r),title=f'({P2} Result{M2} )',style='#ff0000'))
    # Pembagian
    elif oper in ['/']:
        cetak(nel(f'{P2} Anda Menggunakan Operasi Hitung {H2}Pembagian{P2},\n Silahlan Masukkan Angka Yang Ingin Anda\n Bagi.',width=50,style='#ff0000'))
        cetak(nel(f'{P2}             Masukkan Angka Pertama',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        x = input(f'   ╰─>{H} ')
        cetak(nel(f'{P2}              Masukkan Angka Kedua',subtitle=f'{P2}╭─',subtitle_align='left',width=50,style='#ff0000'))
        z = input(f'   ╰─>{H} ')
        r = int(x) / int(z)
        print('')
        cetak(nel.fit('[white]Hasil Dari Pembagian [green]{} [white]Dengan[green] {}[white] Adalah: [green]{}'.format(x,z,r),title=f'({P2} Result {M2})',style='#ff0000'))
    else:
        cetak(f'\n{P2} [{M2}!{P2}] Input Yang Bener Goblok.');exit()

if __name__=='__main__':
    kalkulator()
