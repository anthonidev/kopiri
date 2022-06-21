from PIL import Image
import os


def compress_kopiri(self, quality=60):
    out = "C:/Users/Anthoni/Desktop/AuToPy/out/"
    weight_initial = 0
    weight_final = 0
    weight = 0
    size_sm = 700, 700
    size_xs = 350, 350
    for filename in self.fileName:
        name, extension = os.path.splitext(filename)
        self.textEdit.setText(extension)
        # file name with extension
        name = os.path.basename(filename)
        self.textEdit.setText(name)

        self.textEdit.setText(os.path.splitext(filename)[0])
        if extension == ".jpg":
            weight_initial += os.stat(filename).st_size
            name = name.replace(".jpg", ".webp")
            picture = Image.open(filename).convert("RGB")

            img_sm = Image.open(filename).convert("RGB")
            img_sm.thumbnail(size_sm, Image.ANTIALIAS)
            img_sm.save(out+"thumbnail_"+name,
                        "webp")

            img_xs = Image.open(filename).convert("RGB")
            img_xs.thumbnail(size_xs, Image.ANTIALIAS)

            img_xs.save(out+"thumbnail_"+name,
                        "webp")

            picture.save(out+name,
                         "webp", optimize=True, quality=quality)
            weight = os.stat(out+name).st_size
            while weight > 300000:
                quality -= 1
                picture.save(out+name,
                             "webp", optimize=True, quality=quality)
                weight = os.stat(out+name).st_size
            weight_final += weight
            self.textEdit.setText("Saved: "+name)

    self.textEdit.setText("Initial weight: " +
                          str("{0:.2f}".format(weight_initial/1000000))+" MB")
    self.textEdit.setText(
        "Final weight: "+str("{0:.2f}".format(weight_final/1000000))+" MB")
    self.textEdit.setText("compression: " +
                          str("{0:.2f}".format((weight_initial-weight_final)/weight_initial*100))+"%")
