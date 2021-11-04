from PIL import Image


def main():
    img = Image.open('C:/Users/arthu/Pictures/CAD Canvas/halloween.jpg','r')
    imgWidth, imgHeight = img.size
    img = img.convert('RGBA')
    imgdata = img.getdata()

    print(str(imgWidth) + "," + str(imgHeight))

    xpos = 0
    ypos = 0

    pixel_value = []
    x = []
    y = []

    total_pixels = int(imgWidth)*int(imgHeight)

    convert = [[0 for x in range(imgWidth)] for y in range(imgHeight)]

    height = 50
    height_factor = height / 255

    counter = 1

    outfile = open("halloween.obj","w")

    for pixel in imgdata:
        xpos += 1
        xpos %= imgWidth
        if(xpos == 0):
            ypos += 1
            ypos %= imgHeight
        grey_val = round(0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2],2)
        convert[ypos][xpos] = (str(xpos),str(ypos),str(-grey_val*height_factor), str(counter))
        counter+=1
    vertices = ""
    for row in range(0,imgHeight):
        for col in range(0,imgWidth):
            pixel = convert[row][col]
            vertices += ("v " + pixel[0] + ".0 " + pixel[1] + ".0 " + pixel[2] + "\n")
    max_x_vert = 0
    max_y_vert = 0
    faces = ""
    for row in range(0,imgHeight):
        for col in range(0,imgWidth):
            if(row == 0 and col == 0):
                continue
            if(row+1 >= imgHeight):
                break
            if(col+1 >= imgWidth):
                continue
            pixel = convert[row][col]
            rpixel = convert[row][col+1]
            dpixel = convert[row+1][col]
            rdpixel = convert[row+1][col+1]
            max_x_vert = rdpixel[0]
            max_y_vert = rdpixel[1]
            face = "f " + pixel[3] + " " + rpixel[3] + " " + dpixel[3] + "\n"
            face += "f " + rpixel[3] + " " + dpixel[3] + " " + rdpixel[3] + "\n"
            faces+=(face)
    print (str(max_x_vert) + "," + str(max_y_vert))
    '''
    vertices += "v 0.0 0.0 0.0\n" # top left corner (counter)
    vertices += "v 0.0 " + str(max_y_vert) + " 0.0\n" # bottom left corner
    vertices += "v " + str(max_x_vert) + " 0.0 0.0\n" # top right corner
    vertices += "v " + str(max_x_vert) + ".0 " + str(max_y_vert) + ".0 " + "0.0\n" # bottom right corner
    
    # now generate border around it
    vertices += "v 0.0 0.0 " + str(height) + ".0\n" # top left front corner (counter+4)
    vertices += "v 0.0 " + str(max_y_vert) + ".0 " + str(height) + ".0\n" # bottom left front corner
    vertices += "v " + str(max_x_vert) + ".0 0.0 " + str(height) + ".0\n" # top right front corner
    vertices += "v " + str(max_x_vert) + ".0 " + str(max_y_vert) + ".0 " + str(height) + ".0\n"

    #faces += "f " + str(counter+5) + " " + str(counter+4) + " " + str(counter+6) + "\n"
    #faces += "f " + str(counter+5) + " " + str(counter+7) + " " + str(counter+6) + "\n"
    #faces += "f " + str(counter) + " " + str(counter+4) + " " + str(counter+5) + "\n"
    #faces += "f " + str(counter) + " " + str(counter+1) + " " + str(counter+5) + "\n"
    #faces += "f " + str(counter) + " " + str(counter+4) + " " + str(counter+2) + "\n"
    #faces += "f " + str(counter+2) + " " + str(counter+4) + " " + str(counter+6) + "\n"
    #faces += "f " + str(counter+3) + " " + str(counter+7) + " " + str(counter+6) + "\n"
    #faces += "f " + str(counter+3) + " " + str(counter+7) + " " + str(counter+5) + "\n"
    #faces += "f " + str(counter+2) + " " + str(counter+6) + " " + str(counter+3) + "\n"
    #faces += "f " + str(counter+1) + " " + str(counter+5) + " " + str(counter+3) + "\n"
    '''
    outfile.write(vertices)
    outfile.write(faces)
    
            
main()
    
