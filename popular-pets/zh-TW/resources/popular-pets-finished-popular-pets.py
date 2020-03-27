#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = '最喜歡的動物'
piechart.add('狗', 6)
piechart.add('貓', 4)
piechart.add('倉鼠', 3)
piechart.add('魚', 2)
piechart.add('蛇', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = '最喜歡的動物'
barchart.add('狗', 6)
barchart.add('貓', 4)
barchart.add('倉鼠', 3)
barchart.add('魚', 2)
barchart.add('蛇', 1)
barchart.render()
  
piechart2 = pygal.Pie()
barchart2 = pygal.Bar()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
    barchart2.add(label, int(value))
    
file.close()

#piechart2.render()
#barchart2.render()

butterflies = pygal.Bar()
butterflies.title = '數蝴蝶'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    butterflies.add(label, int(value))
file.close()

butterflies.render()

pn = pygal.Bar()
pn.title = '海盜 vs 忍者'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
