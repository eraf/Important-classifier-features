import pandas as pd
import numpy as np

def best_fit(row, time, fare):
    time_lower = row['mean_time'] - row['std_time']
    time_upper = row['mean_time'] + row['std_time']
    fare_lower = row['mean_fare'] - row['std_fare']
    fare_upper = row['mean_fare'] + row['std_fare']
    if (time_lower < time < time_upper) and (fare_lower < fare < fare_upper):
        return 2
    elif (time_lower < time < time_upper) or (fare_lower < fare < fare_upper):
        return 1
    else:
        return 0

def pick_driver(time, fare, profile_df):
    best_match1 = profile_df.apply(best_fit, axis=1, time = time, fare = fare)
    best_match2 = profile_df['completed_trips'] * profile_df['acr'] #acr means assigned to completed ratio
    k = best_match2.max()*10
    profile_df['best_match'] = k*best_match1 + best_match2
    best_driver_dataset = profile_df.sort_values(by='best_match', ascending=False)
    return best_driver_dataset