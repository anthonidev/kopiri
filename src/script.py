from PIL import Image
import os


def compress_kopiri(fileName, quality=60):
    out = "C:/Users/Anthoni/Desktop/AuToPy/out/"
    weight_initial = 0
    weight_final = 0
    weight = 0
    for filename in fileName:
        name, extension = os.path.splitext(filename)
        print("extension", extension)

        # file name with extension
        name = os.path.basename(filename)
        print("name", name)

        print(os.path.splitext(filename)[0])
        if extension == ".jpg":
            weight_initial += os.stat(filename).st_size
            name = name.replace(".jpg", ".webp")
            picture = Image.open(filename).convert("RGB")
            picture.save(out+name,
                         "webp", optimize=True, quality=quality)
            weight = os.stat(out+name).st_size
            while weight > 300000:
                quality -= 1
                picture.save(out+name,
                             "webp", optimize=True, quality=quality)
                weight = os.stat(out+name).st_size
            weight_final += weight
            print("Saved: "+name)

    print("Initial weight: " +
          str("{0:.2f}".format(weight_initial/1000000))+" MB")
    print("Final weight: "+str("{0:.2f}".format(weight_final/1000000))+" MB")
    print("compression: " +
          str("{0:.2f}".format((weight_initial-weight_final)/weight_initial*100))+"%")
