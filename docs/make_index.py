#!/usr/local/bin/python

""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""
from __future__ import print_function
import os.path, time

INDEX_TEMPLATE = r"""

<html>
<head>
<title>${header}</title>
<meta name="description" content="${header}"/>
</head>
<body>
<h1>Index of ${header}</h1>
<hr>
<pre>
<a href="../">../</a>
% for name in dirnames:
<a href="${name}">${name}/</a>${' ' * (50 - len(name))}${time} ${' ' * (34 - len(time))} -
% endfor
% for name in filenames:
<a href="${name}">${name}</a>${' ' * (50 - len(name))}${time} ${' ' * (34 - len(time))} ${filesize}
% endfor
</pre>
<hr>
</body>
</html>
"""

EXCLUDED = ['index.html', 'make_index.py','copia_repo.sh','.DS_Store']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def fun(dir,rootdir):
    print('Processing: '+dir)
    filenames = [fname for fname in sorted(os.listdir(dir))
              if fname not in EXCLUDED and os.path.isfile(dir+fname)]
    dirnames = [fname for fname in sorted(os.listdir(dir))
            if fname not in EXCLUDED  ]
    dirnames = [fname for fname in dirnames if fname not in filenames]
#    header = os.path.basename(dir)
    f = open(dir+'/index.html','w')
    # time=time.ctime(os.path.getctime(dir)))
    #print time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(dir)))

    #print time.strftime("%a, %d %b %Y %H:%M:%S +0000", os.path.getmtime(dir) )
    print(Template(INDEX_TEMPLATE).render(dirnames=dirnames,filenames=filenames, header=dir,ROOTDIR=rootdir,filesize=os.path.getsize(dir), time=time.ctime(os.path.getctime(dir))),file=f)
    f.close()
    for subdir in dirnames:
        try:
            fun(dir+subdir+"/",rootdir+'../')
        except:
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fun(args.directory+'/','../')

if __name__ == '__main__':
    main()
