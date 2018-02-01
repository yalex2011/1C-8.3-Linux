#! /usr/bin/python
# -*- encoding: utf-8 -*-

import subprocess

def get_rac(*args):

    command = ''
    list1 = []
    dict1 = dict()

    for arg in args:
        command = command + arg + ' '
    #print command
    p = subprocess.Popen( command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
    for line in p.stdout.readlines():
        #line = line.decode('cp1252').encode('utf-8')
        sline = line.split()
        #print sline
        if len(sline) != 0 :
            sline.remove(':')
            if len(sline)==2 :
                 dict1[sline[0]]=sline[1]
            else:
                 dict1[sline[0]]=''
        else:
            list1.append(dict1)
            dict1 = dict()

    retval = p.wait()
    return list1
