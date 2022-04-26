import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

import plotly.graph_objects as go

# data
google = {'google_mydig': [356, 286, 272, 269, 266, 264, 261, 256, 242, 236],
          'google_localdns': [68, 37, 31, 30, 29, 29, 26, 22, 21, 20],
          'google_googledns': [17, 17, 21, 25, 26, 26, 26, 28, 28, 41]}
Youtube = {'Youtube_mydig': [326, 308, 306, 287, 280, 275, 275, 272, 251, 240],
           'Youtube_localdns': [36, 29, 29, 28, 27, 26, 25, 25, 20, 17],
           'Youtube_googledns': [42, 33, 31, 29, 27, 25, 24, 20, 19, 19]}
Baidu = {'Baidu_mydig': [1708, 874, 874, 853, 838, 831, 820, 808, 784, 721],
         'Baidu_localdns': [41, 35, 35, 28, 27, 25, 23, 17, 17, 16],
         'Baidu_googledns': [42, 33, 31, 29, 27, 25, 24, 20, 19, 19], }
zoom = {'Zoom_mydig': [1861, 902, 854, 512, 427, 422, 415, 402, 395, 382],
        'Zoom_localdns': [35, 34, 29, 27, 27, 25, 25, 24, 24, 17],
        'Zoom_googledns': [178, 132, 86, 44, 42, 35, 32, 31, 31, 28], }
weibo = {'Weibo_mydig': [1102, 949, 858, 845, 839, 834, 816, 809, 803, 797],
         'Weibo_localdns': [352, 31, 31, 31, 27, 26, 26, 26, 25, 25],
         'Weibo_googledns': [550, 385, 364, 288, 268, 235, 36, 36, 33, 28], }
reddit = {'Reddit_mydig': [523, 482, 464, 264, 258, 257, 247, 242, 236, 236],
          'Reddit_localdns': [35, 34, 31, 27, 26, 25, 23, 21, 19, 17],
          'Reddit_googledns': [41, 39, 35, 34, 29, 24, 23, 23, 22, 20], }
Bing = {'Bing_mydig': [278, 254, 252, 247, 242, 241, 233, 232, 231, 219],
        'Bing_localdns': [96, 71, 40, 37, 28, 25, 21, 19, 18, 17],
        'Bing_googledns': [35, 31, 28, 27, 22, 22, 19, 19, 18, 15], }
Ins = {'Ins_mydig': [251, 243, 237, 236, 236, 232, 228, 227, 224, 222],
       'Ins_localdns': [161, 43, 37, 35, 31, 31, 30, 26, 26, 21],
       'Ins_googledns': [37, 35, 35, 33, 33, 32, 29, 28, 27, 27], }
Bilibili = {'Bilibili_mydig': [413, 410, 407, 406, 404, 393, 389, 385, 384, 383],
            'Bilibili_localdns': [195, 120, 115, 106, 29, 27, 27, 25, 24, 18],
            'Bilibili_googledns': [35, 35, 34, 34, 34, 33, 33, 32, 25, 25], }
Taobao = {'Taobao_mydig': [398, 392, 391, 387, 387, 379, 370, 366, 365, 357],
          'Taobao_localdns': [29, 29, 28, 28, 27, 24, 24, 23, 21, 17],
          'Taobao_googledns': [34, 29, 26, 26, 23, 21, 20, 19, 19, 14], }

# codes for single plot
# df = pd.DataFrame(Taobao)
#

# fig, ax = plt.subplots(1, 1)
#
# table(ax, np.round(df.describe(), 2),
#       loc='upper right',
#       colWidths=[0.2, 0.2, 0.2, 0.2]
#       )
#
# df.plot.box(title="Taobao query times",
#             ax=ax)
#
# plt.grid(linestyle="--", alpha=0.3)
# plt.show()
#
fig = go.Figure()
x = ['google_mydig', 'google_localdns', 'google_googledns', 'Youtube_mydig', 'Youtube_localdns',
     'Youtube_googledns',
     'Baidu_mydig', 'Baidu_localdns', 'Baidu_googledns', 'Zoom_mydig', 'Zoom_localdns', 'Zoom_googledns',
     'Weibo_mydig',
     'Weibo_localdns', 'Weibo_googledns', 'Reddit_mydig', 'Reddit_localdns', 'Reddit_googledns',
     'Bing_mydig',
     'Bing_localdns',
     'Bing_googledns', 'Ins_mydig', 'Ins_localdns', 'Ins_googledns', 'Bilibili_mydig',
     'Bilibili_localdns', 'Bilibili_googledns', 'Taobao_mydig', 'Taobao_localdns', 'Taobao_googledns',
     'Taobao_mydig', 'Taobao_localdns', 'Taobao_googledns']

fig.add_trace(go.Box(
    x=x,
    y=[356, 286, 272, 269, 266, 264, 261, 256, 242, 236, 326, 308, 306, 287, 280, 275, 275, 272, 251, 240,
       1708, 874, 874, 853, 838, 831, 820, 808, 784, 721, 1861, 902, 854, 512, 427, 422, 415, 402, 395, 382,
       1102, 949, 858, 845, 839, 834, 816, 809, 803, 797, 523, 482, 464, 264, 258, 257, 247, 242, 236, 236,
       523, 482, 464, 264, 258, 257, 247, 242, 236, 236, 251, 243, 237, 236, 236, 232, 228, 227, 224, 222,
       413, 410, 407, 406, 404, 393, 389, 385, 384, 383, 398, 392, 391, 387, 387, 379, 370, 366, 365, 357
       ],
    name='my_dig',
)
)

fig.add_trace(go.Box(
    x=x,
    y=[68, 37, 31, 30, 29, 29, 26, 22, 21, 20, 36, 29, 29, 28, 27, 26, 25, 25, 20, 17,
       41, 35, 35, 28, 27, 25, 23, 17, 17, 16, 35, 34, 29, 27, 27, 25, 25, 24, 24, 17,
       352, 31, 31, 31, 27, 26, 26, 26, 25, 25, 35, 34, 31, 27, 26, 25, 23, 21, 19, 17,
       96, 71, 40, 37, 28, 25, 21, 19, 18, 17, 161, 43, 37, 35, 31, 31, 30, 26, 26, 21,
       195, 120, 115, 106, 29, 27, 27, 25, 24, 18, 29, 29, 28, 28, 27, 24, 24, 23, 21, 17],
    name='localDns'
))

fig.add_trace(go.Box(
    x=x,
    y=[17, 17, 21, 25, 26, 26, 26, 28, 28, 41, 42, 33, 31, 29, 27, 25, 24, 20, 19, 19,
       42, 33, 31, 29, 27, 25, 24, 20, 19, 19, 178, 132, 86, 44, 42, 35, 32, 31, 31, 28,
       550, 385, 364, 288, 268, 235, 36, 36, 33, 28, 550, 385, 364, 288, 268, 235, 36, 36, 33, 28,
       35, 31, 28, 27, 22, 22, 19, 19, 18, 15, 37, 35, 35, 33, 33, 32, 29, 28, 27, 27,
       35, 35, 34, 34, 34, 33, 33, 32, 25, 25, 34, 29, 26, 26, 23, 21, 20, 19, 19, 14],
    name='googleDns'
))

fig.update_layout(
    boxmode='group'
)

fig.show()
