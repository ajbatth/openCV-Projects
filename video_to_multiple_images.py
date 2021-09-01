import cv2

print("Press 0 to open web camera")
print("Press 1 to access connected camera")
cam = int(input())

print("Enter the location of folder where you want to store images:")
location= input()

vid = cv2.VideoCapture(cam,cv2.CAP_DSHOW)
ret,image = vid.read()

count =0

while(vid.isOpened()):
    if ret == True:
        cv2.imwrite(location+"\\img%d.jpg"%count,image )
        vid.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        
        ret, image = vid.read()
        cv2.imshow("res",image)
        print ('Read a new frame:',count ,ret)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
    else:
            break

vid.release() 
cv2.destroyAllWindows()
    

