import random
import time
import datetime
import pandas as pd
import os

# Load existing simulation data from the Excel file if it exists (currently isn't working)
output_excel_path = '/Users/idiaaguebor/Documents/simulation_results.xlsx'
simulation_data_exists = os.path.isfile(output_excel_path)  # Check if the file exists

try:
    simulation_data = pd.read_excel('/Users/idiaaguebor/Documents/simulation_results.xlsx')
except FileNotFoundError:
    # If the file doesn't exist, create an empty DataFrame
    simulation_data = pd.DataFrame()

# Load data from CSV file
data_from_csv = pd.read_csv('/Users/idiaaguebor/Downloads/SAILS ROUTES.csv')

columns = ["Origins", "Destinations", "Class of Service", "Received at Origin Location", "Loaded to Container",
           "Enroute to Next Location", "Events", "Arrived Next Location", "Arrived at Destination",
           "Unloaded from Transport", "Unloaded from Container", "Picked up at Destination"]

simulation_data = pd.DataFrame(columns=columns)

# Enter the events separated by each transportation mode 
event_lists = {
'Ship': [
('Sea Storm/Weather', 'Attempting to go around storms, expected to add approx. 2 hours', 0.15),
('Customs Delays', 'Waiting, expected to add 1 hour', 0.1),
('Port Congestion', 'Waiting until congestion eases, expected to add 2 hours', 0.1),
('Pirate Attack', 'Evading pirates/ Seek naval assistance, expected to add 2 hours', 0.1),
('Engine Failure', 'Fixing engine, expected to add approx. 3 hours', 0.1),
('Tsunami', 'Reroute into deeper waters, expected to add approx. 5 hours', 0.05),
('No Events!', 'Running smoothly', 0.5),
],
'Plane': [
('Severe Turbulence', 'Adjusting to find smoother air course, expected to add approx. 30 minutes', 0.125),
('Air Traffic Delays', 'Circling and wait for the airspace to clear out, expected to add approx. 1 hour', 0.125),
('Aircraft Mechanical Issues', 'Performing an emergency landing, expected to add approx. 48 hours', 0.1),
('Security Threat', 'Landing to respond to security threats, expected to add approx. 24 hours', 0.075),
('Frozen Runway', 'Waiting until runway is clear, expected to add approx. 1 hour', 0.05),
('Bird Strike', 'Landing to tend to damages, expected to add approx. 24 hours', 0.025),
('No Events!', 'Running smoothly', 0.5),
],
'Truck': [
('Traffic Jam(s)', 'Navigating through traffic jams, expected to add approx. 30 minutes', 0.175),
('Hailstorm', 'Waiting for storm to pass, expected to add approx. 1 hour', 0.075),
('Road Closure', 'Planning alternative route, expected to add approx. 2 hours', 0.075),
('Godzilla', 'Rerouting to safety, expected to add approx. 24 hours', 0.025),
('Vehicle Breakdown', 'Dispatching replacement vehicle, expected to add approx. 2 hours', 0.1),
('Highway Robbery', 'Evading robbers/Rerouting to safer route, expected to add approx. 1 hour', 0.05),
('No Events!', 'Running smoothly', 0.5),
],
'Train': [
('Track Maintenance', 'Waiting for maintenance to be completed, expected to add approx. 1 hour', 0.2),
('Derailment', 'Clearing the track and resuming journey, expected to add approx. 3 hours', 0.1),
('Landslide', 'Clearing the track and resuming journey, expected to add approx. 2 hours', 0.05),
('Meteor Strike', 'Stopping to protect cargo, expected to add approx. 24 hours', 0.025),
('Train Robbery', 'Waiting for security to respond to the robbers, expected to add 1 hour', 0.05),
('Wildfires', 'Waiting until wildfires are under control, expected to add approx. 2 hours', 0.075),
('No Events!', 'Running smoothly', 0.5),
],
'Falcon': [
('Launch Delays', 'Handling launch delays, expected to add approx. 1 hour', 0.2),
('Space Debris Collision', 'Avoiding debris until course is cleared', 0.125),
('Solar Flare Activity', 'Waiting until solar flare activities decrease, expected to add approx. 2 hours', 0.05),
('Bird Strike (launch)', 'Assessing and repairing damage prior to launch, expect to add approx. 4 hours', 0.1),
('UFO Encounter', 'Taking safety precautions and reroute, expected to add approx. 4 hours', 0.1),
('ISS Docking Delay', 'Waiting until issues causing delays are clear, expected to add approx. 1 hour', 0.025),
('No Events!', 'Running smoothly', 0.5),
],
'Dragon': [
('Launch Delays', 'Delaying until the issues are resolved, expected to add approx. 1 hour', 0.2),
('Space Debris Collision', 'Avoiding debris until course is clear, expected to add approx. 2 hours', 0.125),
('Solar Flare Activity', 'Waiting until solar flare activities decrease, expected to add approx. 2 hours', 0.05),
('Bird Strike (launch)', 'Assessing and repairing damages prior to launch, expected to add approx. 4 hours', 0.1),
('UFO Encounter', 'Taking safety precautions and rerouting, expected to add approx. 4 hours', 0.1),
('ISS Docking Delay', 'Waiting until issues causing delays are cleared, expected to add approx. 1 hour', 0.025),
('No Events!', 'Running smoothly', 0.5),
],
}


origin_city = input('Enter origin city: ')
destination_city = input('Enter destination city: ')
service_class = input('Enter class of service (Standard, Express, Premium): ')


# Connecting the variables (origin, destination, service class, transportation mode, hours traveled) from the csv
filtered_data = data_from_csv[(data_from_csv['Origin Code'] == origin_city) & 
                              (data_from_csv['Destination Code'] == destination_city) & 
                              (data_from_csv['Class of Service'] == service_class)]

if filtered_data.empty:
    print('No matching records found.')
else:
    for _, journey in filtered_data.iterrows():
        transportation_mode = journey['Transportation ']  
        hours_traveled = int(journey['Hours Traveled'])
        # Defining current time for the time stamps 
        current_time = datetime.datetime.now()

        simulation_data = simulation_data._append({
            'Origins': origin_city,
            'Destinations': destination_city,
            'Class of Service': service_class,
            'Received at Origin Location': current_time.strftime('%m/%d/%Y %I:%M %p'),
            'Loaded to Container': None,
            'Enroute to Next Location': None,
            'Events': None,
            'Arrived Next Location': None,
            'Arrived at Destination': None,
            'Unloaded from Transport': None,
            'Unloaded from Container': None,
            'Picked up at Destination': None
        }, ignore_index=True)       
        
        
# Running through the lifecycles with sleep time and time and date stamps 1 second = 1 hour
        print('Received at Origin Location', current_time.strftime('%m/%d/%Y %I:%M %p'))  # Display in 12-hour clock format
        time.sleep(1)
        current_time += datetime.timedelta(hours=1)  # Add 1 hour

        # Add the loaded to container details to the DataFrame
        print('Loaded to Container', current_time.strftime('%m/%d/%Y %I:%M %p'))
        simulation_data.at[simulation_data.index[-1], 'Loaded to Container'] = current_time.strftime('%m/%d/%Y %I:%M %p')
        time.sleep(3)
        current_time += datetime.timedelta(hours=3)  # Add 3 hours

        # Add the enroute to next location details to the DataFrame
        print('Enroute to Next Location', current_time.strftime('%m/%d/%Y %I:%M %p'))
        
        if hours_traveled == 24:
            time.sleep(24 / 2) 
            current_time += datetime.timedelta(hours=24 /2)  # Add half of travel time
        elif hours_traveled == 384:
            time.sleep(384 / 2)
            current_time += datetime.timedelta(hours=384 / 2)  # Add half of travel time
        elif hours_traveled == 48:
            time.sleep(48 / 2)
            current_time += datetime.timedelta(hours=48 / 2)  # Add half of travel time
        elif hours_traveled == 72:
            time.sleep(72 /2)
            current_time += datetime.timedelta(hours=72/ 2)  # Add half of travel time
        elif hours_traveled == 840:
            time.sleep(840 /2)
            current_time += datetime.timedelta(hours=840/ 2)  # Add half of travel time
        elif hours_traveled == 1152:
            time.sleep(1152 /2)
            current_time += datetime.timedelta(hours=1152/ 2)  # Add half of travel time
        elif hours_traveled == 912:
            time.sleep(912 /2)
            current_time += datetime.timedelta(hours=912/ 2)  # Add half of travel time
        elif hours_traveled == 360:
            time.sleep(360 /2)
            current_time += datetime.timedelta(hours=360/ 2)  # Add half of travel time
        elif hours_traveled == 408:
            time.sleep(408 /2)
            current_time += datetime.timedelta(hours=408/ 2)  # Add half of travel time
        elif hours_traveled == 216:
            time.sleep(216 /2)
            current_time += datetime.timedelta(hours=216/ 2)  # Add half of travel time
        elif hours_traveled == 96:
            time.sleep(96 /2)
            current_time += datetime.timedelta(hours=96/ 2)  # Add half of travel time
        elif hours_traveled == 120:
            time.sleep(120 /2)
            current_time += datetime.timedelta(hours=120/ 2)  # Add half of travel time
        elif hours_traveled == 192:
            time.sleep(192 /2)
            current_time += datetime.timedelta(hours=192/ 2)  # Add half of travel time
        elif hours_traveled == 456:
            time.sleep(456 /2)
            current_time += datetime.timedelta(hours=456/ 2)  # Add half of travel time
        elif hours_traveled == 744:
            time.sleep(744 /2)
            current_time += datetime.timedelta(hours=744/ 2)  # Add half of travel time
        elif hours_traveled == 240:
            time.sleep(240 /2)
            current_time += datetime.timedelta(hours=240/ 2)  # Add half of travel time

        simulation_data.at[simulation_data.index[-1], 'Enroute to Next Location'] = current_time.strftime('%m/%d/%Y %I:%M %p')
     
        event_list = event_lists.get(transportation_mode)
        
        if event_list:
            random_event, response, probability = random.choices(event_list, weights=[prob for _, _, prob in event_list])[0]
            print(f'* Event - {random_event}\n Response: {response} (Probability: {probability * 100}%)')


# Added the events with estimated added hours with time stamps that adjust accordingly
        if "Sea Storm" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Sea Storm
            current_time += datetime.timedelta(hours=2)
        elif "Customs Delays" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Customs Delays
            current_time += datetime.timedelta(hours=1)
        elif "Port Congestion" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Port Congestion
            current_time += datetime.timedelta(hours=2)
        elif "Pirate Attack" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Pirate Attack
            current_time += datetime.timedelta(hours=2)
        elif "Engine Failure" in random_event:
            time.sleep(3)  # Sleep for 3 hours for Engine Failure
            current_time += datetime.timedelta(hours=3)
        elif "Tsunami" in random_event:
            time.sleep(5)  # Sleep for 5 hours for Tsunami
            current_time += datetime.timedelta(hours=5)
        # For Plane events
        elif "Severe Turbulence" in random_event:
            time.sleep(1 / 2)  # Sleep for 30 minutes for Severe Turbulence
            current_time += datetime.timedelta(hours=0.5)
        elif "Air Traffic Delays" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Air Traffic Delays
            current_time += datetime.timedelta(hours=1)
        elif "Aircraft Mechanical Issues" in random_event:
            time.sleep(48)  # Sleep for 48 hours for Aircraft Mechanical Issues
            current_time += datetime.timedelta(hours=48)
        elif "Security Threat" in random_event:
            time.sleep(24)  # Sleep for 24 hours for Security Threat
            current_time += datetime.timedelta(hours=24)
        elif "Frozen Runway" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Frozen Runway
            current_time += datetime.timedelta(hours=1)
        elif "Bird Strike" in random_event:
            time.sleep(24)  # Sleep for 24 hours for Bird Strike
            current_time += datetime.timedelta(hours=24)
        # For Truck events
        elif "Traffic Jam(s)" in random_event:
            time.sleep(1 / 2)  # Sleep for 30 minutes for Traffic Jams
            current_time += datetime.timedelta(hours=0.5)
        elif "Hailstorm" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Hailstorm
            current_time += datetime.timedelta(hours=1)
        elif "Road Closure" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Road Closure
            current_time += datetime.timedelta(hours=2)
        elif "Godzilla" in random_event:
            time.sleep(24)  # Sleep for 24 hours for Godzilla
            current_time += datetime.timedelta(hours=24)
        elif "Vehicle Breakdown" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Vehicle Breakdown
            current_time += datetime.timedelta(hours=2)
        elif "Highway Robbery" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Highway Robbery
            current_time += datetime.timedelta(hours=1)
        # For Train events
        elif "Track Maintenance" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Track Maintenance
            current_time += datetime.timedelta(hours=1)
        elif "Derailment" in random_event:
            time.sleep(3)  # Sleep for 3 hours for Derailment
            current_time += datetime.timedelta(hours=3)
        elif "Landslide" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Landslide
            current_time += datetime.timedelta(hours=2)
        elif "Meteor Strike" in random_event:
            time.sleep(24)  # Sleep for 24 hours for Meteor Strike
            current_time += datetime.timedelta(hours=24)
        elif "Train Robbery" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Train Robbery
            current_time += datetime.timedelta(hours=1)
        elif "Wildfires" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Wildfires
            current_time += datetime.timedelta(hours=2)
        # For Falcon events
        elif "Launch Delays" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Launch Delays
            current_time += datetime.timedelta(hours=1)
        elif "Space Debris Collision" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Space Debris Collision
            current_time += datetime.timedelta(hours=2)
        elif "Solar Flare Activity" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Solar Flare Activity
            current_time += datetime.timedelta(hours=2)
        elif "Bird Strike (launch)" in random_event:
            time.sleep(4)  # Sleep for 4 hours for Bird Strike (launch)
            current_time += datetime.timedelta(hours=4)
        elif "UFO Encounter" in random_event:
            time.sleep(4)  # Sleep for 4 hours for UFO Encounter
            current_time += datetime.timedelta(hours=4)
        elif "ISS Docking Delay" in random_event:
            time.sleep(1)  # Sleep for 1 hour for ISS Docking Delay
            current_time += datetime.timedelta(hours=1)
        # For Dragon events
        elif "Launch Delays" in random_event:
            time.sleep(1)  # Sleep for 1 hour for Launch Delays
            current_time += datetime.timedelta(hours=1)
        elif "Space Debris Collision" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Space Debris Collision
            current_time += datetime.timedelta(hours=2)
        elif "Solar Flare Activity" in random_event:
            time.sleep(2)  # Sleep for 2 hours for Solar Flare Activity
            current_time += datetime.timedelta(hours=2)
        elif "Bird Strike (launch)" in random_event:
            time.sleep(4)  # Sleep for 4 hours for Bird Strike (launch)
            current_time += datetime.timedelta(hours=4)
        elif "UFO Encounter" in random_event:
            time.sleep(4)  # Sleep for 4 hours for UFO Encounter
            current_time += datetime.timedelta(hours=4)
        elif "ISS Docking Delay" in random_event:
            time.sleep(1)  # Sleep for 1 hour for ISS Docking Delay
            current_time += datetime.timedelta(hours=1)
        # For the "No Events!" case
        elif "No Events!" in random_event:
            time.sleep(0)  # Default sleep time for no events
    
        print('Arrived Next Location', current_time.strftime('%m/%d/%Y %I:%M %p'))
        if hours_traveled == 24:
            time.sleep(24 / 2) 
            current_time += datetime.timedelta(hours=24 /2)  # Add half of travel time
        elif hours_traveled == 384:
            time.sleep(384 / 2)
            current_time += datetime.timedelta(hours=384 / 2)  # Add half of travel time
        elif hours_traveled == 48:
            time.sleep(48 / 2)
            current_time += datetime.timedelta(hours=48 / 2)  # Add half of travel time
        elif hours_traveled == 72:
            time.sleep(72 /2)
            current_time += datetime.timedelta(hours=72/ 2)  # Add half of travel time
        elif hours_traveled == 840:
            time.sleep(840 /2)
            current_time += datetime.timedelta(hours=840/ 2)  # Add half of travel time
        elif hours_traveled == 1152:
            time.sleep(1152 /2)
            current_time += datetime.timedelta(hours=1152/ 2)  # Add half of travel time
        elif hours_traveled == 912:
            time.sleep(912 /2)
            current_time += datetime.timedelta(hours=912/ 2)  # Add half of travel time
        elif hours_traveled == 360:
            time.sleep(360 /2)
            current_time += datetime.timedelta(hours=360/ 2)  # Add half of travel time
        elif hours_traveled == 408:
            time.sleep(408 /2)
            current_time += datetime.timedelta(hours=408/ 2)  # Add half of travel time
        elif hours_traveled == 216:
            time.sleep(216 /2)
            current_time += datetime.timedelta(hours=216/ 2)  # Add half of travel time
        elif hours_traveled == 96:
            time.sleep(96 /2)
            current_time += datetime.timedelta(hours=96/ 2)  # Add half of travel time
        elif hours_traveled == 120:
            time.sleep(120 /2)
            current_time += datetime.timedelta(hours=120/ 2)  # Add half of travel time
        elif hours_traveled == 192:
            time.sleep(192 /2)
            current_time += datetime.timedelta(hours=192/ 2)  # Add half of travel time
        elif hours_traveled == 456:
            time.sleep(456 /2)
            current_time += datetime.timedelta(hours=456/ 2)  # Add half of travel time
        elif hours_traveled == 744:
            time.sleep(744 /2)
            current_time += datetime.timedelta(hours=744/ 2)  # Add half of travel time
        elif hours_traveled == 240:
            time.sleep(240 /2)
            current_time += datetime.timedelta(hours=240/ 2)  # Add half of travel time
    
        print('Arrived at Destination Location', current_time.strftime('%m/%d/%Y %I:%M %p'))
        time.sleep(2)
        current_time += datetime.timedelta(hours=2)  # Add 2 hours
        simulation_data.at[simulation_data.index[-1], 'Arrived at Destination'] = current_time.strftime('%m/%d/%Y %I:%M %p')

        print('Unloaded from Transport', current_time.strftime('%m/%d/%Y %I:%M %p'))
        time.sleep(2)
        current_time += datetime.timedelta(hours=2)  # Add 2 hours
        simulation_data.at[simulation_data.index[-1], 'Unloaded from Transport'] = current_time.strftime('%m/%d/%Y %I:%M %p')

        print('Unloaded from Container', current_time.strftime('%m/%d/%Y %I:%M %p'))
        time.sleep(5)
        current_time += datetime.timedelta(hours=5)  # Add 5 hours
        simulation_data.at[simulation_data.index[-1], 'Unloaded from Container'] = current_time.strftime('%m/%d/%Y %I:%M %p')

        print('Picked up at Destination', current_time.strftime('%m/%d/%Y %I:%M %p'))
        simulation_data.at[simulation_data.index[-1], 'Picked up at Destination'] = current_time.strftime('%m/%d/%Y %I:%M %p')

        # Save the DataFrame to an Excel file

output_excel_path = '/Users/idiaaguebor/Documents/simulation_results.xlsx'
simulation_data.to_excel(output_excel_path, index=False)