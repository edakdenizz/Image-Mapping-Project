import cv2
import os


image_path = "C:/Users/edakd/kuş_bakışı_haritalama/mahalle_krokisi.jpg"  


if not os.path.exists(image_path):
    print("Dosya yokk:", image_path)
else:
    
    image = cv2.imread(image_path)

    if image is None:
        print("Görüntü yok.")
    else:
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        
        cv2.imshow("Gri Görüntü", gray_image)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()  