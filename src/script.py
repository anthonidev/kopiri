from PIL import Image
import os


def compress_kopiri(
    fileName,
    th_xm,
    th_sm,
    optimize,
    weight_max,
    quality,
    
    txt_result,
    le_wi,
    le_wf,
    le_reduce,
    le_state,
    progressBar
):
    out = "C:/Users/Anthoni/Desktop/AuToPy/out/"
    weight_initial = 0
    weight_final = 0

    size_sm = 700, 700
    size_xs = 350, 350
    size_main= 1500,1500
    le_state.emit("Compressing...")
    weight = 0

    length = int(100/len(fileName))
    if th_sm:
        length = int(100/(len(fileName)*2))
    if th_xm:
        length = int(100/(len(fileName)*2))
    if th_xm and th_sm:
        length = int(100/(len(fileName)*3))

    # progressBar.setValue(length)
    try:
        bar_progress = 0
        for filename in fileName:
            
            name, extension = os.path.splitext(filename)
            name = os.path.basename(filename)
            if extension == ".jpg":
                weight_initial += os.stat(filename).st_size
                name = name.replace(".jpg", ".webp")
                picture = Image.open(filename).convert("RGB")
                picture.thumbnail(size_main, Image.ANTIALIAS)
                if th_sm:
                    img_sm = Image.open(filename).convert("RGB")
                    img_sm.thumbnail(size_sm, Image.ANTIALIAS)
                    img_sm.save(out+"thumbnail_sm_"+name, "webp")
                   

                    bar_progress += length
                    progressBar.emit(bar_progress)
                    txt_result.emit("Thumbnail SM: "+name)

                if th_xm:
                    th_xm = Image.open(filename).convert("RGB")
                    th_xm.thumbnail(size_xs, Image.ANTIALIAS)
                    th_xm.save(out+"thumbnail_xm_"+name, "webp")
                    txt_result.emit("Thumbnail XM: "+name)

                    bar_progress += length
                    progressBar.emit(bar_progress)

                picture.save(out+name, "webp",
                             optimize=optimize, quality=quality)

                weight = os.stat(out+name).st_size
                
                while weight > weight_max:
                    quality -= 5
                    picture.save(out+name,
                                 "webp", optimize=optimize, quality=quality)
                    weight = os.stat(out+name).st_size
                weight_final += weight
                bar_progress += length
                progressBar.emit(bar_progress)

                
                txt_result.emit("Compressed: "+name)
                
        le_state.emit("Done!")
        progressBar.emit(100)
    except Exception as e:
        le_state.emit("Error")

    le_wi.emit(str("{0:.2f}".format(weight_initial/1000000))+" MB")
    le_wf.emit(str("{0:.2f}".format(weight_final/1000000))+" MB")
    le_reduce.emit(str("{0:.2f}".format(
        (weight_initial-weight_final)/weight_initial*100))+"%")
    