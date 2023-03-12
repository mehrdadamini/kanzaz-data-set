def normalise_logs(df, LogName, sampelWell):

    gr_percentils_05 = df.groupby('Well Name')[LogName].quantile(0.05)
    df['05_PERC'] = df['Well Name'].map(gr_percentils_05)

    gr_percentile_95 = df.groupby('Well Name')[LogName].quantile(0.95)
    df['95_PERC'] = df['Well Name'].map(gr_percentile_95)

    def normalise(curve, ref_low, ref_high, well_low, well_high):
        return ref_low + ((ref_high - ref_low) * ((curve - well_low) / (well_high - well_low)))

    key_well_high = df.groupby('Well Name').get_group(sampelWell)[LogName].max()
    key_well_low = df.groupby('Well Name').get_group(sampelWell)[LogName].min()
    
    df[LogName + '_NORM'] = df.apply(lambda x: normalise(x[LogName], key_well_low, key_well_high, x['05_PERC'], x['95_PERC']), axis=1)

    df = df.drop(labels=["05_PERC" ,'95_PERC'], axis=1)

    return df
