import pandas as pd
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat,Command,NoEscape,NewPage,Foot
from pylatex.utils import italic
import os
import numpy as np
import random

data = pd.read_csv('fgd.csv')

impressions = ['baik','friendly','ceria','ramah','asik']

doc = Document('basic')
doc.documentclass = Command('documentclass',options=['12pt', 'portrait'],arguments=['article'])

doc.preamble.append(Command('title', 'Buku Angkatan FTE19'))
doc.preamble.append(Command('author', 'Developed by Dion Andreas Solang 07211940000039'))
doc.append(NoEscape(r'\maketitle'))
doc.append(NewPage())
doc.append("you can find the source code at https://github.com/messier12/buku_angkatan")
doc.append(NewPage())
for fgd in range(1,61,1):
    working_data=data[data.FGD==fgd]
    image_path = 'img/'+str(fgd)+'.jpg'
    with doc.create(Section('FGD '+str(fgd),numbering=False)):
        with doc.create(Figure(position='h!')) as fgd_pic:
                fgd_pic.add_image(image_path, width='9cm')
        for idx in working_data.index:
            if working_data.NRP[idx] == 7211940000039:
                continue
            doc.append('Nama: '+working_data['Nama'][idx]+'\n')
            doc.append('NRP: '+'0'+str(working_data['NRP'][idx])+'\n')
            doc.append('Asal: '+working_data['Asal'][idx]+'\n')
            doc.append('Hobi: '+working_data['Hobi'][idx]+'\n')
            doc.append('FI : '+random.choice(impressions)+'\n')
            doc.append('CI : '+random.choice(impressions)+'\n\n')
    doc.append(NewPage())

doc.generate_pdf('full', clean_tex=False)
