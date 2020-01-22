# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myapp.models import Document
from myapp.forms import DocumentForm
import numpy as np
from PIL import Image
# import matplotlib.pyplot as plt
import cv2, os
month = 5
# %matplotlib inline

def color_pixal(avg, month):
    if(month>=1 and month<=3):
        if(avg>=60 and avg<=125):
            return 1
    elif(month==4):
        if(avg>=70 and avg<=110):
            return 1
    elif(month>=5 and month<=7):
        if(avg>=15 and avg<=100):
            return 1
    elif(month>=8 and month<=9):
        if(avg>=17 and avg<=120):
            return 1
    elif(month>=10 and month<=11):
        if(avg>=69 and avg<=120):
            return 1
    elif(month==12):
        if(avg>=90 and avg<=150):
            return 1
    else:
        return 0

def doeverything(img):
    harvest = 0
    # print('month is '+ str(month) )
    image_copy = img
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            avg = 0
            for k in range(img.shape[2]):
                avg += img[i][j][k]/3
            if(color_pixal(avg,month)):
                image_copy[i][j][1] = avg
                image_copy[i][j][2] = 0
                image_copy[i][j][0] = 0
                harvest += 1
            else:
                image_copy[i][j][1] = 255
                image_copy[i][j][2] = 255
                image_copy[i][j][0] = 255
    # return image_copy,harvest
    return image_copy

def givemeeverything(originalimage):
    # image = cv2.imread(location)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # month = int(location[61:63])
    img = doeverything(originalimage)
    #original image
    # plt.figure(figsize=(20,15))
    # plt.imshow(image)
    # return img,harvest
    return img

def plotit(img):
    array = (np.random.rand(img.shape[0],img.shape[1])*256).astype(np.uint8)
    img = Image.fromarray(img)
    # plt.figure(figsize=(20,15))
    # plt.imshow(img)
    # img.save('output.jpg')
    return img




def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # newdoc = Document(docfile = request.FILES['docfile'])
            newdoc = Image.open(request.FILES.get('docfile'))

            print( type( np.array(newdoc) ) )
            final_output = plotit ( givemeeverything(np.array(newdoc)) )
            im = Image.fromarray(np.uint8(np.asarray(final_output)))
            im = newdoc
            newdoc.save()
            # final_output.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )




def index(request):
    return render_to_response('myapp/index.html')
