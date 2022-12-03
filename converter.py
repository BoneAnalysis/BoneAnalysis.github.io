
def converter(file, newfile):
    from PIL import Image

    with Image.open(file) as temp:
        
        new = newfile + ".jpg"
        temp.save(new)


