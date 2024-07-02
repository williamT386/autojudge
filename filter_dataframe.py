import pandas as pd

def filter_mcq(df):
    search_strings = ['of the following', 'which of those', 'which conclusion', 
                      'among the following', 'all the following', 
                      'where are we most likely', 'based on the provided information',
                      'which combination', 'among the given options', 
                      'where did they meet', 'which are the possible', 
                      'which statement below', 'what is most likely', 
                      'which of the', 'identify the correct sequence', 
                      'identify the incorrect statement']

    mask = pd.Series([False] * len(df))
    # Update mask for each search string
    for search_string in search_strings:
        mask |= df['Question'].str.contains(search_string, case=False, na=False)
    
    df_with_strings = df[mask]
    df_without_strings = df[~mask]

    return df_with_strings, df_without_strings