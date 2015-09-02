#!/usr/bin/python
import os, sys
import os.path
import re
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# basic static pages
def histdata(request):
    # add file path for each file, one file for each experiment
    datafile = ['E1S_count.txt', 'E2S_count.txt', 'E3S_count.txt']
    datafile_full = []
    for f in datafile:
        datafile_full.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__))) + "/../../static/" + f)
        #if os.path.exists(datafile[i]):
        #    continue
    
    # save gene expression to data
    data_obj = {}
    tid = request.GET.get('tid', '')
    if tid:
        for f in datafile_full:
            fsplit = os.path.split(f)
            dh = open(f, "r")
            line_num = 0
            sample = []
            for line in dh:
                line_num = line_num + 1
                line = line.strip("\n")
                m = line.split("\t")
                if line_num == 1:
                    sample = m[1:]
                if tid == m[0]:
                    data_obj[fsplit[1]] = {}
                    data_obj[fsplit[1]]['sample'] = []
                    data_obj[fsplit[1]]['sample'] = sample
                    data_obj[fsplit[1]]['express'] = []
                    data_obj[fsplit[1]]['express'] = m[1:]
    return JsonResponse(data_obj)

def index(request):
    context = {}
    return render(request, 'index.html', context)
