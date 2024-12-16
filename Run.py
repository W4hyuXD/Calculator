#!/usr/bin/env python3
# Kalkulator Dengan Python
# Coded by WahyuDin Ambia
# Update 16 Dec 2024

import os, time, sys
from time import sleep
from rich import print as cetak
from rich.tree import Tree
from rich.panel import Panel as nel 


P = "\x1b[38;5;231m" # Putih
H = "\x1b[38;5;46m"  # Hijau
M2, H2, K2, P2, B2, U2, O2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#00C8FF]", "[#AF00FF]", "[#00FFFF]"]


def jalan(u):
  for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
  
def language():
  lan = nel(f'\n{P2}     Select the language you want to use\n   ( Pilih Bahasa yang ingin anda gunakan )\n',title=f'({P2} Choose Language {M2})',width=50,style='#ff0000')
  tree = Tree(lan,guide_style='#ff0000')
  tree.add(f'[on #ff0000]{P2} ID [/][/] ({M2} Indonesia{P2} )')
  tree.add(f'[on #0400fd]{P2} EN [/][/] ({B2} English{P2} )')
  cetak(tree)
  choose()

def choose():
  cos = input(f'\nChoice: {H}')
  if cos in ['EN','en']:
    jalan(f'\n {P}[•] Waiting...');time.sleep(1)
    os.system('python3 Main/EN.py')
  elif cos in ['ID','id']:
    jalan(f'\n {P}[•] Tunggu Sebentar...');time.sleep(1)
    os.system('python3 Main/ID.py')
  else:
    cetak(f'{P2}[{M2}!{P2}] Input Yang Bener Kocak.')
    exit()


if __name__=='__main__':
  try:
    os.system('clear')
  except:pass
  time.sleep(3);language()