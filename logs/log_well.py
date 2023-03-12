import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
    
def log_well(logs, top_depth, bottom_depth):
    #make sure logs are sorted by depth
    logs = logs.sort_values(by='Depth')
    
    facies_colors = ['#ffff00', '#B03A2E','#784212','#D35400', '#80ffff','#273746', '#8080ff', '#ff8c00', '#ef138a']
    
    
    cmap_facies = colors.ListedColormap(
            facies_colors[0:len(facies_colors)], 'indexed')
    
    ztop=top_depth; zbot= bottom_depth
    
    cluster=np.repeat(np.expand_dims(logs['Facies'].values,1), 100, 1)
    
    f, ax = plt.subplots(nrows=1, ncols=6, figsize=(25, 15))
    ax[0].plot(logs.GR, logs.Depth, '-g')
    ax[1].plot(logs.ILD_log10, logs.Depth, '-')
    ax[2].plot(logs.DeltaPHI, logs.Depth, '-', color='0.5')
    ax[3].plot(logs.PHIND, logs.Depth, '-', color='r')
    ax[4].plot(logs.PE, logs.Depth, '-', color='black')
    im=ax[5].imshow(cluster, interpolation='none', aspect='auto', cmap=cmap_facies,vmin=1,vmax=9)
    
    divider = make_axes_locatable(ax[5])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar=plt.colorbar(im, cax=cax)
    cbar.set_label((17*' ').join([' SS ', 'CSiS', 'FSiS', 
                                'SiSh', ' MS ', ' WS ', ' D  ', 
                                ' PS ', ' BS ']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')
    
    for i in range(len(ax)-1):
        ax[i].set_ylim(ztop,zbot)
        ax[i].invert_yaxis()
        ax[i].grid()
        ax[i].locator_params(axis='x', nbins=3)
    
    ax[0].set_xlabel("GR")
    ax[0].set_xlim(logs.GR.min(),logs.GR.max())
    ax[1].set_xlabel("ILD_log10")
    ax[1].set_xlim(logs.ILD_log10.min(),logs.ILD_log10.max())
    ax[2].set_xlabel("DeltaPHI")
    ax[2].set_xlim(logs.DeltaPHI.min(),logs.DeltaPHI.max())
    ax[3].set_xlabel("PHIND")
    ax[3].set_xlim(logs.PHIND.min(),logs.PHIND.max())
    ax[4].set_xlabel("PE")
    ax[4].set_xlim(logs.PE.min(),logs.PE.max())
    ax[5].set_xlabel('Facies')
    
    ax[1].set_yticklabels([]); ax[2].set_yticklabels([]); ax[3].set_yticklabels([])
    ax[4].set_yticklabels([]); ax[5].set_yticklabels([])
    ax[5].set_xticklabels([])
    f.suptitle('Well: %s'%logs.iloc[0]['Well Name'], fontsize=14,y=0.94)
    
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

def compare_facies_plot(logs, compadre, top_depth, bottom_depth):
     #make sure logs are sorted by depth
    logs = logs.sort_values(by='Depth')
    
    facies_colors = ['#ffff00', '#B03A2E','#784212','#D35400', '#80ffff','#273746', '#8080ff', '#ff8c00', '#ef138a']
    
    
    cmap_facies = colors.ListedColormap(
            facies_colors[0:len(facies_colors)], 'indexed')
    
    ztop=top_depth; zbot= bottom_depth
    
    cluster=np.repeat(np.expand_dims(logs['Facies'].values,1), 100, 1)
    
    #make sure logs are sorted by depth
    logs = logs.sort_values(by='Depth')
    cmap_facies = colors.ListedColormap(
            facies_colors[0:len(facies_colors)], 'indexed')
    
    ztop=logs.Depth.min(); zbot=logs.Depth.max()
    
    cluster1 = np.repeat(np.expand_dims(logs['Facies'].values,1), 100, 1)
    cluster2 = np.repeat(np.expand_dims(logs[compadre].values,1), 100, 1)
    
    f, ax = plt.subplots(nrows=1, ncols=7, figsize=(25, 15))
    ax[0].plot(logs.GR, logs.Depth, '-g')
    ax[1].plot(logs.ILD_log10, logs.Depth, '-')
    ax[2].plot(logs.DeltaPHI, logs.Depth, '-', color='0.5')
    ax[3].plot(logs.PHIND, logs.Depth, '-', color='r')
    ax[4].plot(logs.PE, logs.Depth, '-', color='black')
    im1 = ax[5].imshow(cluster1, interpolation='none', aspect='auto',
                    cmap=cmap_facies,vmin=1,vmax=9)
    im2 = ax[6].imshow(cluster2, interpolation='none', aspect='auto',
                    cmap=cmap_facies,vmin=1,vmax=9)
    
    divider = make_axes_locatable(ax[6])
    cax = divider.append_axes("right", size="20%", pad=0.05)
    cbar=plt.colorbar(im2, cax=cax)
    cbar.set_label((17*' ').join([' SS ', 'CSiS', 'FSiS', 
                                'SiSh', ' MS ', ' WS ', ' D  ', 
                                ' PS ', ' BS ']))
    cbar.set_ticks(range(0,1)); cbar.set_ticklabels('')
    
    for i in range(len(ax)-2):
        ax[i].set_ylim(ztop,zbot)
        ax[i].invert_yaxis()
        ax[i].grid()
        ax[i].locator_params(axis='x', nbins=3)
    
    ax[0].set_xlabel("GR")
    ax[0].set_xlim(logs.GR.min(),logs.GR.max())
    ax[1].set_xlabel("ILD_log10")
    ax[1].set_xlim(logs.ILD_log10.min(),logs.ILD_log10.max())
    ax[2].set_xlabel("DeltaPHI")
    ax[2].set_xlim(logs.DeltaPHI.min(),logs.DeltaPHI.max())
    ax[3].set_xlabel("PHIND")
    ax[3].set_xlim(logs.PHIND.min(),logs.PHIND.max())
    ax[4].set_xlabel("PE")
    ax[4].set_xlim(logs.PE.min(),logs.PE.max())
    ax[5].set_xlabel('Facies')
    ax[6].set_xlabel(compadre)
    
    ax[1].set_yticklabels([]); ax[2].set_yticklabels([]); ax[3].set_yticklabels([])
    ax[4].set_yticklabels([]); ax[5].set_yticklabels([])
    ax[5].set_xticklabels([])
    ax[6].set_xticklabels([])
    f.suptitle('Well: %s'%logs.iloc[0]['Well Name'], fontsize=14,y=0.94)