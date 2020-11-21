import cv2
import os
from threading import Timer
import time

cap = cv2.VideoCapture(0)        #打开摄像头
# cap.set(3, 1080)
# cap.set(4, 960)
cap.set(3, 640)
cap.set(4, 480)

if os.path.exists("D:/sys/path/time/temp/asf/39123") == False:
    os.makedirs("D:/sys/path/time/temp/asf/39123")
    
def r_s(): 

    try:
        cap = cv2.VideoCapture(0)        #打开摄像头

        name = str(time.time())
        print("name => " + name)
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)     #生成摄像头窗口
        
        # if cv2.waitKey(1) & 0xFF == ord('q'):   #如果按下q 就截图保存并退出#
        cv2.imwrite("D:/sys/path/time/temp/asf/39123/"+name+".png", frame)   #保存路径
        print("saved")

                # break

        cap.release()

    except Exception as e:

        print(e)

    finally:

        t = Timer(1, r_s)
        t.start()
        print("Timer END")

try:

    r_s()
        
    cv2.destroyAllWindows()

except Exception as e:

    print(e)