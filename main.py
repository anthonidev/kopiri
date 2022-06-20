from PIL import Image
import os

gallery = "C:/Users/Anthoni/Desktop/AuToPy/gallery/"
out = "C:/Users/Anthoni/Desktop/AuToPy/out/"
weight_initial = 0
weight_final = 0

if __name__ == "__main__":
    for filename in os.listdir(gallery):
        name, extension = os.path.splitext(gallery+filename)

        if extension == ".jpg":
            weight_initial += os.stat(gallery+filename).st_size
            name = filename.replace(".jpg", ".webp")
            picture = Image.open(gallery+filename).convert("RGB")
            picture.save(out+name,
                         "webp", optimize=True, quality=50)
            weight_final += os.stat(out+name).st_size
            print("Saved: "+name)


print("Initial weight: "+str("{0:.2f}".format(weight_initial/1000000))+" MB")
print("Final weight: "+str("{0:.2f}".format(weight_final/1000000))+" MB")
print("compression: " +
      str("{0:.2f}".format((weight_initial-weight_final)/weight_initial*100))+"%")
