import pandas as pd 

# Load the dataset 
data = pd.read_csv('data.csv')
print("Dataset loaded: ")
print(data)

# Assumptions 
distance_km = 2.5   # Length of road segment in kilometres 
free_flow_speed = 50  # ideal speed in km/h (speed limit)

# Calculate free flow travel time in minutes 
free_flow_time = (distance_km / free_flow_speed) * 60 
print(f'\nFree flow travel time: {free_flow_time:.1f} minutes')

# Calculate actual travel time for each row 
data['travel_time_mins'] = (distance_km/ data['avg_speed']) * 60 
data['travel_time_mins'] = data['travel_time_mins'].round(1)
print("\nTravel times: ")
print(data[['time', 'avg_speed', 'travel_time_mins']])

# Calculate delay 
data['delay_mins']= (data['travel_time_mins']- free_flow_time)
data['delay_mins'] = data['delay_mins'].round(1)
print(f"\nDelay_mins: ")
print(data[['time', 'avg_speed', 'travel_time_mins', 'delay_mins']])

def classify_delay(delay):
    if delay < 1: 
        return "Minimal"
    elif 1 < delay < 3: 
        return "Moderate"
    else: return "Severe"

data['delay_severity'] = data['delay_mins'].apply(classify_delay)

print("\nDelay severity:")
print(data[['time', 'avg_speed', 'travel_time_mins', 'delay_mins', 'delay_severity']])

data.to_csv('output.csv', index=False)
print("\nResults saved to output.csv")