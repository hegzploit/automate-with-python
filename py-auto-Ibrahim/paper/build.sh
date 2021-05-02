#!/usr/bin/bash

./generate_data.py
./plot.py -i data.dat -o plot-data.png
pdflatex paper.tex
zathura paper.pdf 