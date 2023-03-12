import matplotlib.pyplot as plt

def multywelllog(wells, logname):

    fig, ax = plt.subplots(figsize=(8,6))

    for label, df in wells:
       df[logname].plot(kind ='kde', ax=ax, label=label)
       plt.xlim(df[logname].min(), df[logname].max())

    plt.grid(True)
    plt.legend()
    plt.show()

 



