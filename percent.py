from sklearn.cluster import KMeans
import cv2
import numpy as np
import pandas as pd

index = ["color","color_name","hex","r","g","b"]
csv = pd.read_csv('colors.csv',names = index, header = None)

def getcolorname(r,g,b):
    minimum = 100000000000
    for i in range(len(csv)):
        d = abs(r-int(csv.loc[i,"r"]))+abs(g-int(csv.loc[i,"g"]))+abs(b-int(csv.loc[i,"b"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]

    return cname

def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
    z = []
    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent*100)
        #cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        z.append(endX - startX)
        startX = endX
    return z

def percentage(name, num):
    #path = r'D:\Documents\Desktop\DRDO_Project\colorpicpng.png'
    image = cv2.imread(name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters = num)
    clt.fit(image)

    cent = clt.cluster_centers_
    #print(cent.shape)
    hist = centroid_histogram(clt)
    bar = plot_colors(hist, cent)
    #bar1 = bar
    colname = []
    for i in range(num):
        R = cent[i][0]
        G = cent[i][1]
        B = cent[i][2]
        colname.append(getcolorname(R,G,B))
        n = i
        #print(str(n)+"\n\n")

    fin = {}
    #print(len(colname))
    for i in range(len(colname)):
        #print(i)
        fin[colname[i]] = bar[i]
        #print(len(fin))
        #bar.remove(j)
        #break
    
    #print(len(fin.shape))
    return fin