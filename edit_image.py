import cv2


print("  WELCOME TO IMAGE EDITOR  ".center(80,'#'),end="\n\n")
print("Enter the path of image you want to edit:- ",end="")
path= input()

print("Press 1 for coloured output\nPress 0 for Gray-Scale Output\nPress -1 for Unchanged")
Type=int(input())

img = cv2.imread(path,Type)
img = cv2.resize(img, (img.shape[1],800))

cv2.imshow("WindoW", img)

cv2.waitKey(5000) & 0xFF

print("Press 0 to flip up-down")
print("Press 1 to flip left-right")
print("Press -1 to flip left-right && top-down")
print("Press 2 for NO CHANGE")

FLIP=int(input())
if FLIP in (-1,0,1):    
    img2=cv2.flip(img,FLIP)
else:
    img2=img  

print("Press \"q\" to exit withot saving")
print("Press \"s\" to save image")
comnd=input()
if comnd=='s':
    print("Enter the path location where you want to save image:")
    path_output=input()
    cv2.imwrite(path_output, img2) 
    cv2.destroyAllWindows()

    

cv2.destroyAllWindows()