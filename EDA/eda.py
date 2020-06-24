# This function accepts a Pandas DataFrame as an argument and returns a detailed exploratory analysis (numerical) for user
def descriptive_eda(dataset):
    import statistics
    from scipy import stats
    import pandas as pd
    Variable, Count, Missing_Values, Missing_Values_Percentage, Minimum, P1, P5, P10, P25, Mean, Median, Mode, P75, P90, P95, P99, Maximum, \
    ShapiroWilk_Statistics, ShapiroWilk_Statistics_P_Value, KolmogorovSmirnov_Statistics, \
    KolmogorovSmirnov_Statistics_P_Value = ([] for i in range(21))
    char_summary = pd.DataFrame()
    headers = ['Label', 'Frequency']
    for i in dataset.columns: 
        if dataset[i].dtypes == 'float64':
            Variable.append(i)
            Count.append(len(dataset[i]))
            Missing_Values.append(dataset[i].isnull().sum())
            Missing_Values_Percentage.append((dataset[i].isnull().sum()/len(dataset[i])*100))
            Minimum.append(dataset[i].min())
            P1.append(dataset[i].quantile(0.01))
            P5.append(dataset[i].quantile(0.05))
            P10.append(dataset[i].quantile(0.1))
            P25.append(dataset[i].quantile(0.25))
            P75.append(dataset[i].quantile(0.75))
            P90.append(dataset[i].quantile(0.9))
            P95.append(dataset[i].quantile(0.95))
            P99.append(dataset[i].quantile(0.99))
            Mean.append(dataset[i].mean())
            Median.append(dataset[i].median())
            Maximum.append(dataset[i].max())
            Mode.append(statistics.mode(dataset[i]))
            ShapiroWilk_Statistics.append(stats.shapiro(dataset[i])[0])
            ShapiroWilk_Statistics_P_Value.append(stats.shapiro(dataset[i])[1])
            KolmogorovSmirnov_Statistics.append(stats.kstest(dataset[i], 'norm')[0])
            KolmogorovSmirnov_Statistics_P_Value.append(stats.kstest(dataset[i], 'norm')[1])
            output_df = pd.DataFrame(list(zip(Variable, Count, Missing_Values, Missing_Values_Percentage, Minimum, P1, P5, P10, P25, \
            Mean, Median, Mode, P75, P90, P95, P99, Maximum, \
            ShapiroWilk_Statistics, ShapiroWilk_Statistics_P_Value, KolmogorovSmirnov_Statistics, \
            KolmogorovSmirnov_Statistics_P_Value)), columns = ['Variable', 'Count', 'Missing_Values', 'Missing_Values_Percentage', 'Minimum', \
            'P1', 'P5', 'P10', 'P25', 'Mean', 'Median', 'Mode', 'P75', 'P90', 'P95', 'P99', 'Maximum', \
            'ShapiroWilk_Statistics', 'ShapiroWilk_Statistics_P_Value', 'KolmogorovSmirnov_Statistics', \
            'KolmogorovSmirnov_Statistics_P_Value'])
        if dataset[i].dtypes == 'object':
            idata = pd.DataFrame(dataset[i].value_counts().reset_index())
            idata.columns = headers
            idata['Percentage'] = round(idata['Frequency']/idata['Frequency'].sum()*100, 2)
            idata['Variable'] = i
            char_summary = char_summary.append(idata, ignore_index = True)
    return output_df.round(4), char_summary                


# Example
Numeric_Summary, Character_Summary = descriptive_eda(pandas_dataframe)

