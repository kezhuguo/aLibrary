# Provides color codes for n-color histograms.

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches



### global variables
# uptoN, colordict

uptoN = 7



### Color code conversions

def hex_to_rgb(hexcode):
    return tuple(int(hexcode.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
# fhandle.write('RGB = {}'.format( tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) ))

# print(hex_to_rgb('#B4FBB8'))

def rgb_to_hex(rgb):
    r, g, b = rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# print(rgb_to_hex([255, 165, 1]))

def rgb_to_float(rgb):
    # r, g, b = rgb
    if rgb[0].__class__ == list:
        result = [[(x / 255) for x in y] for y in rgb]
        # for y in result:
        #     print(list(y))
    else:
        result = [(x / 255) for x in rgb]
        # print(result)
    return result

# c = [[164,200,217],
#      [108,150,204],
#      [237,174,146],
#      [201,35,33]]

# rgb_to_float(c)
# print()
# rgb_to_float([164,200,217])



### Color palatte

colordict = {}

# two colors
colordict[2] = [[[200,215,235],[250,235,199]],
[[159,201,223],[241,225,199]],
[[140,163,195],[210,173,168]]]

# three colors
colordict[3] = [['#828D93','#EDB176','#78C2E0'],
['#D87070','#7D9BE5','#F5D78F']]

# four colors
colordict[4] = [[[164,200,217],[108,150,204],[237,174,146],[201,35,33]]]

# five colors
colordict[5] = [['#F0A780','#E79397','#97C8AF','#96B6D8','#A797DA'],
['#9281DD','#B7617D','#E4B112','#B7DB29','#159FD7']]

# six colors
colordict[6] = [['#e1703c','#f2bf9e','#4091cf','#a1c6e7','#8cba54','#ccddae']]

# seven colors
colordict[7] = [[[191,193,165],[246,198,246],[152,202,247],[255,248,171],[205,192,219],[160,221,175],[248,211,169]],
['#818181','#2A5522','#BF9895','#E07E35','#F2CCA0','#A9C4E6','#D1392B']]



### Library functions

def plot_all_at_n(nbins):
    binwidth = 1
    if nbins not in colordict:
        print("Error! No palatte for " + str(nbins) + " colors")
    else:
        # nsets = len(colordict[nbins])
        for colorset in colordict[nbins]:
            if colorset[0].__class__ == list:
                codetype = 'rgb'
                newcolorset = rgb_to_float(colorset)
                # # print(colorset)
                # for x in colorset:
                #     x = [str(y) for y in x]
                #     print(','.join(x))
                # # colorset = [','.join(x) for x in colorset]
            else:
                codetype = 'hex'
                newcolorset = colorset
            print(codetype)
            print(colorset)

            # plt.figure(figsize=(6,6))
            # scale = 1.5
            scale = 1
            fig, ax = plt.subplots(figsize=(nbins*scale,scale))
            data = [x+1 for x in range(nbins)]
            binning = [x+0.5 for x in range(nbins)]
            binning.append(nbins + 0.5)
            N, bins, patches = ax.hist(data, edgecolor='white', linewidth=10, bins=binning)
            
            for i in range(len(patches)):
                patches[i].set_facecolor(newcolorset[i])
                # ax.set(xlim=(0, nbins))
                # ax.text(data[i] - binwidth/2, - binwidth/2, codetype, ha='left')
                # ax.text(data[i], - binwidth, str(colorset[i]), ha='center')

            ax.set_axis_off()
            plt.show()

def show_galary():
    for ncolor in range(1, uptoN + 1):
        plot_all_at_n(ncolor)
        print()





### Reference

# https://mp.weixin.qq.com/s?__biz=MzkzNzQxMjQ4MA==&mid=2247488559&idx=2&sn=f3cf5dedf0d9b9ad67f88e574fc569b3&chksm=c28e86c0f5f90fd6f02b64757c91a590bc0d23f8c1a680a5faea1b1cb80906d035c53aac9877&scene=21#wechat_redirect

# https://mp.weixin.qq.com/s?__biz=MzkzNzQxMjQ4MA==&mid=2247488081&idx=1&sn=2679ac1bba33339e02bcd5abf00bfbcb&chksm=c28e80bef5f909a8c2e110a64ca9da2a18e427d6792220945ea7094c589e7cdfc355efdbaacc&scene=21#wechat_redirect

# https://mp.weixin.qq.com/s?__biz=MzkzNzQxMjQ4MA==&mid=2247488984&idx=1&sn=da835daadfcef282e87cb2ff47c5925f&chksm=c28e8737f5f90e21912a53d58385777079640ec4b119809d464954ec75a7650e6fa830533ddf&scene=21#wechat_redirect

# https://mp.weixin.qq.com/s?__biz=MzkzNzQxMjQ4MA==&mid=2247489398&idx=1&sn=8a38171dc61d2d8fe9578a50a492081d&chksm=c28e8599f5f90c8f92d65d1fcb0e758b06e25bac6af04559adbe557c5ce3265d60286acd6dec&scene=21#wechat_redirect

# https://mp.weixin.qq.com/s/p3zngb9V7PTfvukmXeq8xw

