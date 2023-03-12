import numpy as np

def display_cm(conf, target):
    
    facies_labels = ['SS', 'CSiS', 'FSiS', 'SiSh', 'MS',
                 'WS', 'D','PS', 'BS']
    
    if len(conf) < len(facies_labels):
        conf = np.c_[ conf, np.zeros(8) ]
        conf = np.insert(conf, 8, np.zeros(9), axis=0)
    # labels = np.ndarray([0])
    # for i in np.sort(target.unique()):
    #     labels = np.append(labels, facies_labels[i-1])
    labels = facies_labels
    precision = np.diagonal(conf)/conf.sum(axis=0).astype('float')
    recall = np.diagonal(conf)/conf.sum(axis=1).astype('float')
    F1 = 2 * (precision * recall) / (precision + recall)

    precision[np.isnan(precision)] = 0
    recall[np.isnan(recall)] = 0
    F1[np.isnan(F1)] = 0

    precision = np.around(precision, decimals=2)
    recall = np.around(recall, decimals=2)
    F1 = np.around(F1, decimals=2)

    total_precision =  np.around(np.sum(precision * conf.sum(axis=1)) / conf.sum(axis=(0,1)), decimals=2)
    total_recall =  np.around(np.sum(recall * conf.sum(axis=1)) / conf.sum(axis=(0,1)), decimals=2)
    total_F1 =  np.around(np.sum(F1 * conf.sum(axis=1)) / conf.sum(axis=(0,1)), decimals=2)


    # Print header
    print("          " + " Pred", end="")
    for label in labels: 
        b = ' '
        b = b * (5)
        print('%s' % (b), label, end="")
    print (' Total')

    print ("          " + " True")

    # print body
    a = 0
    for i in labels:
        b = ' '
        b = b * (5 - len(i))
        print('         %s' % (b), i, end="")
        for j in range(len(conf)):
            c = ' '
            c = c * (5 + (len(labels[j]) - len(str(conf[a][j]))))
            print('%s' % (c), conf[a][j], end='')
        c = ' '
        c = c * (5 - len(str(sum(conf[a,:]))))
        print('%s' % (c), sum(conf[a,:]))
        a = a + 1

    print()

    # print footer
    print("      Precision", end="")
    a = 0
    for i in precision:
        c = ' '
        c = c * (5 + (len(str(labels[a])) - len(str(i))))
        print('%s' % (c), i, end='')
        a = a+1

    c = ' '
    c = c * (5 - len(str(total_precision)))
    print('%s' % (c), total_precision)


    print("         Recall", end="")
    a = 0
    for i in recall:
        c = ' '
        c = c * (5 + (len(str(labels[a])) - len(str(i))))
        print('%s' % (c), i, end='')
        a = a+1

    c = ' '
    c = c * (5 - len(str(total_recall)))
    print('%s' % (c), total_recall)


    print("             F1", end="")
    a = 0
    for i in F1:
        c = ' '
        c = c * (5 + (len(str(labels[a])) - len(str(i))))
        print('%s' % (c), i, end='')
        a = a+1

    c = ' '
    c = c * (5 - len(str(total_F1)))
    print('%s' % (c), total_F1)

def display_adj_cm(conf, target, adjacent_facies):
    
    facies_labels = ['SS', 'CSiS', 'FSiS', 'SiSh', 'MS',
                 'WS', 'D','PS', 'BS']
    
    if len(conf) < len(facies_labels):
        conf = np.c_[ conf, np.zeros(8) ]
        conf = np.insert(conf, 8, np.zeros(9), axis=0)
    # labels = np.ndarray([0])
    # for i in np.sort(target.unique()):
    #     labels = np.append(labels, facies_labels[i-1])
    labels = facies_labels
        
    nb_classes = conf.shape[0]
    for i in np.arange(0, nb_classes):
        for j in adjacent_facies[i]:
            conf[i][i] += conf[i][j]
            conf[i][j] = 0


    precision = np.diagonal(conf)/conf.sum(axis=0).astype('float')
    recall = np.diagonal(conf)/conf.sum(axis=1).astype('float')
    F1 = 2 * (precision * recall) / (precision + recall)

    precision[np.isnan(precision)] = 0
    recall[np.isnan(recall)] = 0
    F1[np.isnan(F1)] = 0

    precision = np.around(precision, decimals=2)
    recall = np.around(recall, decimals=2)
    F1 = np.around(F1, decimals=2)

    total_precision =  np.around(np.sum(precision * conf.sum(axis=1)) / conf.sum(axis=(0,1)), decimals=2)
    total_recall =  np.around(np.sum(recall * conf.sum(axis=1)) / conf.sum(axis=(0,1)), decimals=2)
    total_F1 =  np.around(np.sum(F1 * conf.sum(axis=1)) / conf.sum(axis=(0,1)), decimals=2)


    # Print header
    print("          " + " Pred", end="")
    for label in labels: 
        b = ' '
        b = b * (5)
        print('%s' % (b), label, end="")
    print (' Total')

    print ("          " + " True")

    # print body
    a = 0
    for i in labels:
        b = ' '
        b = b * (5 - len(i))
        print('         %s' % (b), i, end="")
        for j in range(len(conf)):
            c = ' '
            c = c * (5 + (len(labels[j]) - len(str(conf[a][j]))))
            print('%s' % (c), conf[a][j], end='')
        c = ' '
        c = c * (5 - len(str(sum(conf[a,:]))))
        print('%s' % (c), sum(conf[a,:]))
        a = a + 1

    print()

    # print footer
    print("      Precision", end="")
    a = 0
    for i in precision:
        c = ' '
        c = c * (5 + (len(str(labels[a])) - len(str(i))))
        print('%s' % (c), i, end='')
        a = a+1

    c = ' '
    c = c * (5 - len(str(total_precision)))
    print('%s' % (c), total_precision)


    print("         Recall", end="")
    a = 0
    for i in recall:
        c = ' '
        c = c * (5 + (len(str(labels[a])) - len(str(i))))
        print('%s' % (c), i, end='')
        a = a+1

    c = ' '
    c = c * (5 - len(str(total_recall)))
    print('%s' % (c), total_recall)


    print("             F1", end="")
    a = 0
    for i in F1:
        c = ' '
        c = c * (5 + (len(str(labels[a])) - len(str(i))))
        print('%s' % (c), i, end='')
        a = a+1

    c = ' '
    c = c * (5 - len(str(total_F1)))
    print('%s' % (c), total_F1)