#!/usr/bin/python

import os, sys
import os.path
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def hist(request):
