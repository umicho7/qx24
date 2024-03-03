import pandas as pd
import numpy as np
from numpy.random import default_rng

rng=default_rng()

# Define features
features = ['timestamp', 'vehicle_id', 'signal_strength', 'network_type', 'scenario','upload_spd','download_spd']

# Generate synthetic data
num_samples = 300

data = {
    'timestamp': pd.date_range(start='2024-01-01', periods=num_samples, freq='1T'),
    'vehicle_id': rng.choice(350, size=num_samples, replace=False),
    'network_type': np.random.choice(['2G', '3G', '4G', '5G'], num_samples),
    'scenario': np.random.choice(['tunnel', 'ferry', 'border'], num_samples),
    'signal_strength' : np.random.randint(0,10,size = num_samples),
    'upload_spd' : np.random.uniform(0,10,size = num_samples),
    'download_spd' : np.random.uniform(0,10,size = num_samples)
}
print(len(data['scenario']))

for i, network_type in enumerate(data['network_type']):
    if network_type == '2G':
        if data["scenario"][i] == 'tunnel':
            data['upload_spd'][i] = round(np.random.uniform(0.066, 0.10), 3)
        elif data["scenario"][i] == 'border':
            data['upload_spd'][i] = round(np.random.uniform(0.033, 0.066), 3)
        elif data["scenario"][i] == 'ferry':
            data['upload_spd'][i] = round(np.random.uniform(0.01, 0.033), 3)
        data['download_spd'][i] = data['upload_spd'][i] + round(np.random.uniform(-0.01, 0.01), 3)
    elif network_type == '3G':
        if data["scenario"][i] == 'tunnel':
            data['upload_spd'][i] = round(np.random.uniform(6.66, 10), 3)
        elif data["scenario"][i] == 'border':
            data['upload_spd'][i] = round(np.random.uniform(3.33, 6.66), 3)
        elif data["scenario"][i] == 'ferry':
            data['upload_spd'][i] = round(np.random.uniform(1, 3.33), 3)
        data['download_spd'][i] = data['upload_spd'][i] + round(np.random.uniform(-1, 1), 3)
    elif network_type == '4G':
        if data["scenario"][i] == 'tunnel':
            data['upload_spd'][i] = round(np.random.uniform(77, 100), 3)
        elif data["scenario"][i] == 'border':
            data['upload_spd'][i] = round(np.random.uniform(52, 77), 3)
        elif data["scenario"][i] == 'ferry':
            data['upload_spd'][i] = round(np.random.uniform(30, 52), 3)
        data['download_spd'][i] = data['upload_spd'][i] + round(np.random.uniform(-7, 7), 3)
    elif network_type == '5G':
        if data["scenario"][i] == 'tunnel':
            data['upload_spd'][i] = round(np.random.uniform(200, 250), 3)
        elif data["scenario"][i] == 'border':
            data['upload_spd'][i] = round(np.random.uniform(150, 200), 3)
        elif data["scenario"][i] == 'ferry':
            data['upload_spd'][i] = round(np.random.uniform(100, 150), 3)
        data['download_spd'][i] = data['upload_spd'][i] + round(np.random.uniform(-15, 15), 3)

for i in range (len(data['network_type'])):
    if data["scenario"][i] == 'tunnel':
        if ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.033:
            data["signal_strength"][i] = np.random.randint(-80, -73, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.066:
            data["signal_strength"][i] = np.random.randint(-73, -67, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.10:
            data["signal_strength"][i] = np.random.randint(-67, -60, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 3.33:
            data["signal_strength"][i] = np.random.randint(-80, -73, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 6.66:
            data["signal_strength"][i] = np.random.randint(-73, -67, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 10:
            data["signal_strength"][i] = np.random.randint(-67, -60, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 53:
            data["signal_strength"][i] = np.random.randint(-80, -73, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 76:
            data["signal_strength"][i] = np.random.randint(-73, -67, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 100:
            data["signal_strength"][i] = np.random.randint(-67, -60, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 150:
            data["signal_strength"][i] = np.random.randint(-80, -73, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 200:
            data["signal_strength"][i] = np.random.randint(-73, -67, size = 1)
        else:
            data["signal_strength"][i] = np.random.randint(-67, -60, size = 1)
    elif data["scenario"][i] == 'border' : 
        if ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.033:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.066:
            data["signal_strength"][i] = np.random.randint(-85, -80, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.10:
            data["signal_strength"][i] = np.random.randint(-80, -75, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 3.33:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 6.66:
            data["signal_strength"][i] = np.random.randint(-85, -80, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 10:
            data["signal_strength"][i] = np.random.randint(-80, -75, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 53:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 76:
            data["signal_strength"][i] = np.random.randint(-85, -80, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 100:
            data["signal_strength"][i] = np.random.randint(-80, -75, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 150:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 200:
            data["signal_strength"][i] = np.random.randint(-85, -80, size = 1)
        else:
            data["signal_strength"][i] = np.random.randint(-80, -75, size = 1)
    elif data["scenario"][i] == 'ferry' :
        if ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.033:
            data["signal_strength"][i] = np.random.randint(-100, -95, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.066:
            data["signal_strength"][i] = np.random.randint(-95, -90, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 0.10:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 3.33:
            data["signal_strength"][i] = np.random.randint(-100, -95, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 6.66:
            data["signal_strength"][i] = np.random.randint(-95, -90, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 10:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 53:
            data["signal_strength"][i] = np.random.randint(-100, -95, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 76:
            data["signal_strength"][i] = np.random.randint(-95, -90, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 100:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 150:
            data["signal_strength"][i] = np.random.randint(-100, -95, size = 1)
        elif ((data['upload_spd'][i] + data['download_spd'][i])/2) <= 200:
            data["signal_strength"][i] = np.random.randint(-95, -90, size = 1)
        else:
            data["signal_strength"][i] = np.random.randint(-90, -85, size = 1)


# Introduce anomalies or specific events
df = pd.DataFrame(data, columns=features)
# Save the dataset to a CSV file
df.to_csv('signal_strength_dataset_new.csv', index=False)
