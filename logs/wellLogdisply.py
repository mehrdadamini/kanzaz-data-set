import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def lithology_plot():
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

def makeplot(well, top_depth, bottom_depth):
  fig, ax = plt.subplots(figsize=(20,10))

  #Set up the plot axes
  ax1 = plt.subplot2grid((1,6), (0,0), rowspan=1, colspan = 1)
  ax2 = plt.subplot2grid((1,6), (0,1), rowspan=1, colspan = 1, sharey = ax1)
  ax3 = plt.subplot2grid((1,6), (0,2), rowspan=1, colspan = 1, sharey = ax1)
  ax4 = plt.subplot2grid((1,6), (0,3), rowspan=1, colspan = 1, sharey = ax1)
  ax5 = plt.subplot2grid((1,6), (0,4), rowspan=1, colspan = 1, sharey = ax1)
  ax6 = plt.subplot2grid((1,6), (0,5), rowspan=1, colspan = 1, sharey = ax1)

  # As our curve scales will be detached from the top of the track,
  # this code adds the top border back in without dealing with splines
  ax10 = ax1.twiny()
  ax10.xaxis.set_visible(False)
  ax11 = ax2.twiny()
  ax11.xaxis.set_visible(False)
  ax12 = ax3.twiny()
  ax12.xaxis.set_visible(False)
  ax13 = ax4.twiny()
  ax13.xaxis.set_visible(False)
  ax14 = ax5.twiny()
  ax14.xaxis.set_visible(False)
  ax15 = ax6.twiny()
  ax15.xaxis.set_visible(False)

  # Gamma Ray track
  ax1.plot(well["GR"], well['Depth'], color = "green", linewidth = 2)
  ax1.set_xlabel("Gamma")
  ax1.xaxis.label.set_color("green")
  ax1.set_xlim(well['GR'].min()-10,well['GR'].max()+10)
  ax1.set_ylabel("Depth (m)")
  ax1.tick_params(axis='x', colors="green")
  ax1.spines["top"].set_edgecolor("green")
  ax1.title.set_color('green')
  ax1.set_xticks([well['GR'].min()-10, (well['GR'].max()+10)/4, (well['GR'].max()+10)/2, 3*(well['GR'].max()+10)/4, well['GR'].max()+10])

  # resistivity logging track
  ax2.plot(well["ILD_log10"], well['Depth'], color = "red", linewidth = 2)
  ax2.set_xlabel("resistivity")
  ax2.xaxis.label.set_color("red")
  ax2.set_xlim(well['ILD_log10'].min()-10,well['ILD_log10'].max()+10)
  ax2.tick_params(axis='x', colors="red")
  ax2.spines["top"].set_edgecolor("red")
  ax2.title.set_color('red')
  ax2.set_xticks([well['ILD_log10'].min()-10, (well['ILD_log10'].max()+10)/4, (well['ILD_log10'].max()+10)/2, 3*(well['ILD_log10'].max()+10)/4, well['ILD_log10'].max()+10])

  # photoelectric effect track
  ax3.plot(well["PE"], well['Depth'], color = "blue", linewidth = 2)
  ax3.set_xlabel("photoelectric")
  ax3.xaxis.label.set_color("blue")
  ax3.set_xlim(well['DeltaPHI'].min()-10,well['DeltaPHI'].max()+10)
  ax3.tick_params(axis='x', colors="blue")
  ax3.spines["top"].set_edgecolor("blue")
  ax3.title.set_color('blue')
  ax3.set_xticks([well['PE'].min()-10, (well['PE'].max()+10)/4, (well['PE'].max()+10)/2, 3*(well['PE'].max()+10)/4, well['PE'].max()+10])

  # neutron-density porosity difference track
  ax4.plot(well["DeltaPHI"], well['Depth'], color = "0.5", linewidth = 2)
  ax4.set_xlabel("neutron-density")
  ax4.xaxis.label.set_color('0.5')
  ax4.set_xlim(well['DeltaPHI'].min()-10,well['DeltaPHI'].max()+10)
  ax4.tick_params(axis='x', colors='0.5')
  ax4.spines["top"].set_edgecolor('0.5')
  ax4.title.set_color('0.5')
  ax4.set_xticks([well['DeltaPHI'].min()-10, (well['DeltaPHI'].max()+10)/4, (well['DeltaPHI'].max()+10)/2, 3*(well['DeltaPHI'].max()+10)/4, well['DeltaPHI'].max()+10])

  # average neutron-density porosity track
  ax5.plot(well["PHIND"], well['Depth'], color = "purple", linewidth = 2)
  ax5.set_xlabel("neutron-density")
  ax5.xaxis.label.set_color("purple")
  ax5.set_xlim(well['PHIND'].min()-10,well['PHIND'].max()+10)
  ax5.tick_params(axis='x', colors="purple")
  ax5.spines["top"].set_edgecolor("purple")
  ax5.title.set_color('purple')
  ax5.set_xticks([well['PHIND'].min()-10, (well['PHIND'].max()+10)/4, (well['PHIND'].max()+10)/2, 3*(well['PHIND'].max()+10)/4, well['PHIND'].max()+10])

  # Lithology track
  ax6.plot(well["Facies"], well['Depth'], color = "black", linewidth = 2)
  ax6.set_xlabel("Lithology")
  ax6.set_xlim(0, 1)
  ax6.xaxis.label.set_color("black")
  ax6.tick_params(axis='x', colors="black")
  ax6.spines["top"].set_edgecolor("black")

  for key in lithology_numbers.keys():
    color = lithology_numbers[key]['color']
    hatch = lithology_numbers[key]['hatch']
    ax6.fill_betweenx(well['Depth'], 0, well['Facies'], where=(well['Facies']==key), facecolor=color, hatch=hatch)    

  ax6.set_xticks([0, 1])

  # Common functions for setting up the plot can be extracted into
  # a for loop. This saves repeating code.
  for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.set_ylim(bottom_depth, top_depth)
    ax.grid(which='major', color='lightgrey', linestyle='-')
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.spines["top"].set_position(("axes", 1.02))    
        
  for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    plt.setp(ax.get_yticklabels(), visible = True)
      
  plt.tight_layout()
  fig.subplots_adjust(wspace = 0.15)
