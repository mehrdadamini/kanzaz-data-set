import pandas as pd
import matplotlib.pyplot as plt
def lithologydisply():
    
    lithology_numbers = {1 : {'lith':'S.S.' ,'lith_num':1 , 'hatch':'..' , 'color':'#ffff00' },
                     2 : {'lith':'CoarseSiltstone' ,'lith_num':2 , 'hatch':'-.' , 'color':'#B03A2E' },
                     3 : {'lith':'Fine Siltstone' ,'lith_num':3 , 'hatch':'-..' , 'color':'#784212' },
                     4 : {'lith':'Shaley Siltstone' ,'lith_num':4 , 'hatch':'--' , 'color':'#D35400' },
                     5 : {'lith':'Mudstone' ,'lith_num':5 , 'hatch':'+' , 'color':'#80ffff' },
                     6 : {'lith':'Wackstone' ,'lith_num':6 , 'hatch':'x' , 'color':'#273746' },
                     7 : {'lith':'Dolomite' ,'lith_num':7 , 'hatch':'-/' , 'color':'#8080ff' },
                     8 : {'lith':'Packstone' ,'lith_num':8 , 'hatch':'||' , 'color':'#ff8c00' },
                     9 : {'lith':'Bafflestone' ,'lith_num':9 , 'hatch':'-|' , 'color':'#ef138a' }}

    df_lith = pd.DataFrame.from_dict(lithology_numbers, orient='index')
    df_lith.index.name = 'LITHOLOGY'

    y = [0, 1]
    x = [1, 1]

    fig, axes = plt.subplots(ncols=3,nrows=3,sharex=True,sharey=True,figsize=(10,5),subplot_kw={'xticks':[],'yticks':[]})
    
    for ax, key in zip(axes.flat, lithology_numbers.keys()):
        ax.plot(x, y)
        ax.fill_betweenx(y, 0, 1, facecolor=lithology_numbers[key]['color'], hatch=lithology_numbers[key]['hatch'])
        ax.set_xlim(0, 0.1)
        ax.set_ylim(0, 1)
        ax.set_title(str(lithology_numbers[key]['lith']))
    
    plt.tight_layout()
    return plt.show()