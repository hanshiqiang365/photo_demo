#author: hanshiqiang365 （微信公众号：韩思工作室）

import os
import exifread

def getExif(filename):
    FIELD = 'EXIF DateTimeOriginal'
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    if FIELD in tags:
        print("\nstr(tags[FIELD]): %s" %(str(tags[FIELD]))) 
        #print("\nstr(tags[FIELD]).replace(':', '').replace(' ', '_'): %s" %(str(tags[FIELD]).replace(':', '').replace(' ', '_'))) 
        #print("\nos.path.splitext(filename)[1]: %s" %(os.path.splitext(filename)[1])) 
    else:
        print('No {} found'.format(FIELD),' in: ', filename)
        
photofile_name = "testphoto.jpg"
getExif(photofile_name)

