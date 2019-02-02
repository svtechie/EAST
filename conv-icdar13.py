import glob
import csv
import time
import os

def get_texts():
    files = []
    for ext in ['txt']:
        files.extend(glob.glob(os.path.join('downloads/icdar/icdar-training13', '*.{}'.format(ext))))
        files.extend(glob.glob(os.path.join('downloads/icdar/icdar-test13', '*.{}'.format(ext))))
    return files

def handleFile(p):
    '''
    load annotation from the text file
    :param p:
    :return:
    '''
    if not os.path.exists(p):
        return np.array(text_polys, dtype=np.float32)

    print (p)
    txtop = p.replace(os.path.basename(p).split('.')[1], 'txt15')
    of = open(txtop, "w")
    with open(p, 'r') as f:
        for l in f:
            # Split
            l = l.replace('\n', '')
            line1 = l.split()
            line2 = l.split(', ')
            line3 = l.split(',')
            if len(line2) >= 5 :
                line = line2
            elif len(line3) >= 5 :
                line = line3
            else :
                line = line1

            label = line[-1]
            # strip BOM. \ufeff for python3,  \xef\xbb\bf for python2
            line = [i.strip('\ufeff').strip('\xef\xbb\xbf') for i in line]

            tlx, tly, brx, bry = list(map(float, line[:4]))
            poly = [tlx, tly, brx, tly, brx, bry, tlx, bry]

            str1  = ','.join(str(item) for item in poly)
            str1 += ',' + label
            of.write(str1 + "\n")

    of.close()

filelist = get_texts()

for fn in filelist :
    handleFile(fn)
