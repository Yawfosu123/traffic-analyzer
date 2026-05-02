import pandas as pd

data = pd.read_csv('data.csv')
print(data)


# Printing the average speed column
avg_speed = data['avg_speed']
print(avg_speed)


# Calculating the mean average speed
avg_speed_mean = data['avg_speed'].mean()
print("Mean avg speed:", avg_speed_mean)


# Computing the peak hour
# Finding the maximum vehicle_count and returning the corresponding time
peak_hour = data['vehicle_count'].max()
print("Peak vehicle count:", peak_hour)

lowest_hour = data['vehicle_count'].min()
print("Lowest vehicle count:", lowest_hour)

corresponding_time = data[data['vehicle_count'] == peak_hour]['time']
print("Peak hour time:", corresponding_time)


# Congestion rule
def classify_congestion(speed):
    if speed <= 30:
        return 'Congested'
    else:
        return 'Free Flow'

data['congestion_status'] = data['avg_speed'].apply(classify_congestion)
print(data[['time', 'avg_speed', 'congestion_status']])