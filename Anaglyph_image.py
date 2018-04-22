#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 04:22:31 2017

@authors: Rishabh Sharma & Vishal Nand

"""

from PIL import Image,ImageChops
import numpy
import subprocess

# Function to convert a single two dimensional image to an anaglyph.
'''
The parameter for this function are following
img1: This is the 2D image
shift: This parameter is the number of pixels that the user wants in his image
to be shifted.
'''
def anaglyph_2d_3d(img1,shift):
    width, height = img1.size
    
    img_left = img1
    img_left = numpy.array(img_left)
    img_right = img1
    img_right = numpy.array(img_right)
    
    #removing the blue and green channels from the left image
    img_left[:,:,0] *= 0
#    img_left[:,:,2] *= 0
            
    #removing the blue and green channels from the right image
    img_right[:,:,1] *= 0
    img_right[:,:,2] *= 0
    #creating a container for the anaglyphed logo with the shift.
    final_image = numpy.zeros((height,width+shift,3),'uint8')
    
    '''
    Loop to set the channels in the container with the the desired channel 
    value.
    '''
#    for i in range(0,width):
#        for j in range(0,height):
#            final_image[j,i,0] = img_left[j,i,0]
#            final_image[j,i+shift,1] = img_right[j,i,1]
#            final_image[j,i+shift,2] = img_right[j,i,2]
    for i in range(0,width):
        for j in range(0,height):
            final_image[j,i+shift,0] = img_right[j,i,0]
            final_image[j,i,1] = img_left[j,i,1]
            final_image[j,i,2] = img_left[j,i,2]
    img = Image.fromarray(final_image)
#     final_image = final_image.crop((shift,0,final_image.size[0],final_image.size[1]))
    img = img.crop((shift+5,shift,img.size[0]-shift-5,img.size[1]-shift))
    return img



#function to create anaglyph images from stereo images.
'''
The parameters for the images are following
left: This parameter takes the left image
right: This parameter is the right image
crop: This parameter is the number of pixels that should be cropped from the
left and right image to remove the extra layer.
'''

def anaglyph_from_stereo_images(left, right, crop_size):
    width, height = left.size
    
    #Cropping the region that is not common in both images
    left = left.crop((crop_size,0,left.size[0],left.size[1]))
    right = right.crop((0,0,right.size[0]-crop_size,right.size[1]))
    
    #reading images into an array to get all the channels
    left = numpy.array(left)
    right = numpy.array(right)
    
    #removing the blue and green channels from the left image
    left[:,:,1] *= 0
    left[:,:,2] *= 0
    
    #removing the red channel from the right image
    right[:,:,0] *= 0
    
    #changing the arrays into images with red and cyan filters.
    left = Image.fromarray(left)
    right = Image.fromarray(right)
    
    
    #superimposing the images and creating a single image out of two images with
    #anaglyph effect.
    img = ImageChops.screen(left,right)
    
    return img




def main():
    # modified by Vishal to hard code the filenames generated from Objective C
    #img_left = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_left.png")
    #img_right = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_right.png")

    img_left = Image.open("/Users/Vishal/Downloads/Canon/Left/Left.JPG")
    img_right = Image.open("/Users/Vishal/Downloads/Canon/Right/Right.JPG")

    #Commented the below 3 loc since no logo images currently
    anaglyph_logo_girl_scout = anaglyph_2d_3d(Image.open("/Users/Vishal/Downloads/Canon/Large_GSOC.jpg"),15)
    anaglyph_logo_ACM = anaglyph_2d_3d(Image.open("/Users/Vishal/Downloads/Canon/Large_ACM.jpg"),15)
    anaglyph_logo_CSUF = anaglyph_2d_3d(Image.open("/Users/Vishal/Downloads/Canon/Large_CSUF.jpg"),15) 

    '''
    deviation = 0
    #modified devialtion condition from 300 to 80 and starting value from 50 to 0
    while deviation<=80:
        anaglyph_object_image = anaglyph_from_stereo_images(img_left, img_right,deviation)
        
        #Commented the below 3 loc since no logo images currently
        
        #anaglyph_object_image.paste(anaglyph_logo_girl_scout,(0,0))
        #anaglyph_object_image.paste(anaglyph_logo_ACM,(anaglyph_object_image.size[0]-anaglyph_logo_ACM.size[0],0))
        #anaglyph_object_image.paste(anaglyph_logo_CSUF,(anaglyph_object_image.size[0]-anaglyph_logo_CSUF.size[0],anaglyph_object_image.size[1]-anaglyph_logo_CSUF.size[1]))
        
        anaglyph_object_image.save("/Users/Vishal/Downloads/Canon/img4_anaglyph_with_logo_"+str(deviation)+".jpg")
        deviation += 10
    '''
    anaglyph_object_image = anaglyph_from_stereo_images(img_left, img_right,250)
    anaglyph_object_image.paste(anaglyph_logo_girl_scout,(0,150))
    anaglyph_object_image.paste(anaglyph_logo_ACM,(anaglyph_object_image.size[0]-anaglyph_logo_ACM.size[0],150))
    anaglyph_object_image.paste(anaglyph_logo_CSUF,(anaglyph_object_image.size[0]-anaglyph_logo_CSUF.size[0],anaglyph_object_image.size[1]-(anaglyph_logo_CSUF.size[1]+150)))
    anaglyph_object_image.save("/Users/Vishal/Downloads/Canon/img4_anaglyph.jpg")

    

#displaying the anagyph
def displayAnaglyph():
    cmd1 = 'open img4_anaglyph.jpg'
    anaglyph = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
    output, err = anaglyph.communicate()
	
if __name__ == '__main__':
    main()
    displayAnaglyph()


