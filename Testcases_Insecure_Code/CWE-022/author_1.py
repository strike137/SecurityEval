import os
def deleteImage(request):
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    fileName = request.args.get('fileName')
    os.remove(fileName)
