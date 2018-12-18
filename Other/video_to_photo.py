import cv2
cap = cv2.VideoCapture('E:\\t.mkv')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps =cap.get(cv2.CAP_PROP_FPS)
#fps=30

size=(960,544) #分辨率
i=0
while(cap.isOpened()):
    i=i+1
    print('正在转换第%s张')
    ret, frame = cap.read()
    if ret==True:
        cv2.imwrite('E:/test/'+str(i)+'.jpg',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
print('转换完成')
