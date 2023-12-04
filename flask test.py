# app.py
from flask import Flask, request, jsonify
import datetime,time
import random

app = Flask(__name__)

data = [
    {"Origin Code": "ABZ", "Destination Code": "CHS", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 384},
    {"Origin Code": "ANC", "Destination Code": "SEA", "Transportation": "Train", "Class of Service": "Standard",
     "Hours Traveled": 72},
    {"Origin Code": "ANC", "Destination Code": "SEA", "Transportation": "Train", "Class of Service": "Express",
     "Hours Traveled": 48},
    {"Origin Code": "ANC", "Destination Code": "SEA", "Transportation": "Train", "Class of Service": "Premium",
     "Hours Traveled": 24},
    {"Origin Code": "ATL", "Destination Code": "CLT", "Transportation": "Train", "Class of Service": "Standard",
     "Hours Traveled": 48},
    {"Origin Code": "ATL", "Destination Code": "CLT", "Transportation": "Truck", "Class of Service": "Express",
     "Hours Traveled": 24},
    {"Origin Code": "ATL", "Destination Code": "CLT", "Transportation": "Plane", "Class of Service": "Premium",
     "Hours Traveled": 24},
    {"Origin Code": "BOM", "Destination Code": "EDI", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 840},
    {"Origin Code": "BOM", "Destination Code": "IAH", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 1152},
    {"Origin Code": "BOM", "Destination Code": "CHS", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 912},
    {"Origin Code": "BOM", "Destination Code": "SYD", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 360},
    {"Origin Code": "BOM", "Destination Code": "KUL", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 408},
    {"Origin Code": "BOM", "Destination Code": "SIN", "Transportation": "Ship", "Class of Service": "Standard",
     "Hours Traveled": 216},
    {"Origin Code": "BOM", "Destination Code": "HYD", "Transportation": "Truck", "Class of Service": "Express",
     "Hours Traveled": 72},
    {"Origin Code": "BOM", "Destination Code": "HYD", "Transportation": "Train", "Class of Service": "Premium",
     "Hours Traveled": 48},
    {"Origin Code": "BOM", "Destination Code": "HYD", "Transportation": "Plane", "Class of Service": "Premium",
     "Hours Traveled": 24}, ]

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
        (
        'Air Traffic Delays', 'Circling and wait for the airspace to clear out, expected to add approx. 1 hour', 0.125),
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
        (
        'Solar Flare Activity', 'Waiting until solar flare activities decrease, expected to add approx. 2 hours', 0.05),
        ('Bird Strike (launch)', 'Assessing and repairing damage prior to launch, expect to add approx. 4 hours', 0.1),
        ('UFO Encounter', 'Taking safety precautions and reroute, expected to add approx. 4 hours', 0.1),
        ('ISS Docking Delay', 'Waiting until issues causing delays are clear, expected to add approx. 1 hour', 0.025),
        ('No Events!', 'Running smoothly', 0.5),
    ],
    'Dragon': [
        ('Launch Delays', 'Delaying until the issues are resolved, expected to add approx. 1 hour', 0.2),
        ('Space Debris Collision', 'Avoiding debris until course is clear, expected to add approx. 2 hours', 0.125),
        (
        'Solar Flare Activity', 'Waiting until solar flare activities decrease, expected to add approx. 2 hours', 0.05),
        ('Bird Strike (launch)', 'Assessing and repairing damages prior to launch, expected to add approx. 4 hours',
         0.1),
        ('UFO Encounter', 'Taking safety precautions and rerouting, expected to add approx. 4 hours', 0.1),
        ('ISS Docking Delay', 'Waiting until issues causing delays are cleared, expected to add approx. 1 hour', 0.025),
        ('No Events!', 'Running smoothly', 0.5),
    ],
}


def generate_data(origin, destination, service_class):
    # # Prompting user input
    # origin = input('Enter origin: ')
    # destination = input('Enter destination: ')
    # service_class = input('Enter class of service (Standard, Express, Premium): ')

    # Connecting the variables (origin, destination, service_class, transportation_mode, hours_traveled) with the data manually entered
    filtered_data = [d for d in data if d['Origin Code'] == origin
                     and d['Destination Code'] == destination and d['Class of Service'] == service_class]

    if not filtered_data:
        print('No matching records found.')
    else:
        for d in filtered_data:
            transportation_mode = d['Transportation']
            hours_traveled = int(d['Hours Traveled'])

            # Defining current time for the time stamps
            current_time = datetime.datetime.now()

            # Initialize variables to store timestamps
            origin_timestamp = None
            container_loaded_timestamp = None
            enroute_timestamp = None
            destination_arrival_timestamp = None
            unloaded_transport_timestamp = None
            unloaded_container_timestamp = None
            picked_up_destination_timestamp = None

            # Running through the lifecycles with sleep time and time and date stamps 1 second = 1 hour
            origin_timestamp = current_time
            print('Received at Origin Location',
                  current_time.strftime('%m/%d/%Y %I:%M %p'))  # Display in 12-hour clock format
            #time.sleep(1)
            current_time += datetime.timedelta(hours=1)  # Add 1 hour
            container_loaded_timestamp = current_time
            print('Loaded to Container',
                  current_time.strftime('%m/%d/%Y %I:%M %p'))  # Display in 12-hour clock format
            #time.sleep(3)
            current_time += datetime.timedelta(hours=3)  # Add 1 hour
            enroute_timestamp = current_time
            print('Enroute to Next Location', current_time.strftime('%m/%d/%Y %I:%M %p'))
            # Added the routes travel time with time stamps that adjust
            if hours_traveled == 24:
                # #time.sleep(24 / 2)
                current_time += datetime.timedelta(hours=24 / 2)  # Add half of travel time
            elif hours_traveled == 384:
                # #time.sleep(384 / 2)
                current_time += datetime.timedelta(hours=384 / 2)  # Add half of travel time
            elif hours_traveled == 48:
                # #time.sleep(48 / 2)
                current_time += datetime.timedelta(hours=48 / 2)  # Add half of travel time
            elif hours_traveled == 72:
                # #time.sleep(72 / 2)
                current_time += datetime.timedelta(hours=72 / 2)  # Add half of travel time
            elif hours_traveled == 840:
                # #time.sleep(840 / 2)
                current_time += datetime.timedelta(hours=840 / 2)  # Add half of travel time
            elif hours_traveled == 1152:
                # #time.sleep(1152 / 2)
                current_time += datetime.timedelta(hours=1152 / 2)  # Add half of travel time
            elif hours_traveled == 912:
                # #time.sleep(912 / 2)
                current_time += datetime.timedelta(hours=912 / 2)  # Add half of travel time
            elif hours_traveled == 360:
                # #time.sleep(360 / 2)
                current_time += datetime.timedelta(hours=360 / 2)  # Add half of travel time
            elif hours_traveled == 408:
                # #time.sleep(408 / 2)
                current_time += datetime.timedelta(hours=408 / 2)  # Add half of travel time
            elif hours_traveled == 216:
                # #time.sleep(216 / 2)
                current_time += datetime.timedelta(hours=216 / 2)  # Add half of travel time
            elif hours_traveled == 96:
                # #time.sleep(96 / 2)
                current_time += datetime.timedelta(hours=96 / 2)  # Add half of travel time
            elif hours_traveled == 120:
                # #time.sleep(120 / 2)
                current_time += datetime.timedelta(hours=120 / 2)  # Add half of travel time
            elif hours_traveled == 192:
                # #time.sleep(192 / 2)
                current_time += datetime.timedelta(hours=192 / 2)  # Add half of travel time
            elif hours_traveled == 456:
                # #time.sleep(456 / 2)
                current_time += datetime.timedelta(hours=456 / 2)  # Add half of travel time
            elif hours_traveled == 744:
                # #time.sleep(744 / 2)
                current_time += datetime.timedelta(hours=744 / 2)  # Add half of travel time
            elif hours_traveled == 240:
                # #time.sleep(240 / 2)
                current_time += datetime.timedelta(hours=240 / 2)  # Add half of travel time
            event_list = event_lists.get(transportation_mode)

            if event_list:
                random_event, response, probability = \
                    random.choices(event_list, weights=[prob for _, _, prob in event_list])[0]
                print(f'* Event - {random_event}\n Response: {response} (Probability: {probability * 100}%)')

            # Added the events with estimated added hours with time stamps that adjust accordingly
            if "Sea Storm" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Sea Storm
                current_time += datetime.timedelta(hours=2)
            elif "Customs Delays" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Customs Delays
                current_time += datetime.timedelta(hours=1)
            elif "Port Congestion" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Port Congestion
                current_time += datetime.timedelta(hours=2)
            elif "Pirate Attack" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Pirate Attack
                current_time += datetime.timedelta(hours=2)
            elif "Engine Failure" in random_event:
                #time.sleep(3)  # Sleep for 3 hours for Engine Failure
                current_time += datetime.timedelta(hours=3)
            elif "Tsunami" in random_event:
                #time.sleep(5)  # Sleep for 5 hours for Tsunami
                current_time += datetime.timedelta(hours=5)
            # For Plane events
            elif "Severe Turbulence" in random_event:
                #time.sleep(1 / 2)  # Sleep for 30 minutes for Severe Turbulence
                current_time += datetime.timedelta(hours=0.5)
            elif "Air Traffic Delays" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Air Traffic Delays
                current_time += datetime.timedelta(hours=1)
            elif "Aircraft Mechanical Issues" in random_event:
                #time.sleep(48)  # Sleep for 48 hours for Aircraft Mechanical Issues
                current_time += datetime.timedelta(hours=48)
            elif "Security Threat" in random_event:
                #time.sleep(24)  # Sleep for 24 hours for Security Threat
                current_time += datetime.timedelta(hours=24)
            elif "Frozen Runway" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Frozen Runway
                current_time += datetime.timedelta(hours=1)
            elif "Bird Strike" in random_event:
                #time.sleep(24)  # Sleep for 24 hours for Bird Strike
                current_time += datetime.timedelta(hours=24)
            # For Truck events
            elif "Traffic Jam(s)" in random_event:
                #time.sleep(1 / 2)  # Sleep for 30 minutes for Traffic Jams
                current_time += datetime.timedelta(hours=0.5)
            elif "Hailstorm" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Hailstorm
                current_time += datetime.timedelta(hours=1)
            elif "Road Closure" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Road Closure
                current_time += datetime.timedelta(hours=2)
            elif "Godzilla" in random_event:
                #time.sleep(24)  # Sleep for 24 hours for Godzilla
                current_time += datetime.timedelta(hours=24)
            elif "Vehicle Breakdown" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Vehicle Breakdown
                current_time += datetime.timedelta(hours=2)
            elif "Highway Robbery" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Highway Robbery
                current_time += datetime.timedelta(hours=1)
            # For Train events
            elif "Track Maintenance" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Track Maintenance
                current_time += datetime.timedelta(hours=1)
            elif "Derailment" in random_event:
                #time.sleep(3)  # Sleep for 3 hours for Derailment
                current_time += datetime.timedelta(hours=3)
            elif "Landslide" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Landslide
                current_time += datetime.timedelta(hours=2)
            elif "Meteor Strike" in random_event:
                #time.sleep(24)  # Sleep for 24 hours for Meteor Strike
                current_time += datetime.timedelta(hours=24)
            elif "Train Robbery" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Train Robbery
                current_time += datetime.timedelta(hours=1)
            elif "Wildfires" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Wildfires
                current_time += datetime.timedelta(hours=2)
            # For Falcon events
            elif "Launch Delays" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Launch Delays
                current_time += datetime.timedelta(hours=1)
            elif "Space Debris Collision" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Space Debris Collision
                current_time += datetime.timedelta(hours=2)
            elif "Solar Flare Activity" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Solar Flare Activity
                current_time += datetime.timedelta(hours=2)
            elif "Bird Strike (launch)" in random_event:
                #time.sleep(4)  # Sleep for 4 hours for Bird Strike (launch)
                current_time += datetime.timedelta(hours=4)
            elif "UFO Encounter" in random_event:
                #time.sleep(4)  # Sleep for 4 hours for UFO Encounter
                current_time += datetime.timedelta(hours=4)
            elif "ISS Docking Delay" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for ISS Docking Delay
                current_time += datetime.timedelta(hours=1)
            # For Dragon events
            elif "Launch Delays" in random_event:
                #time.sleep(1)  # Sleep for 1 hour for Launch Delays
                current_time += datetime.timedelta(hours=1)
            elif "Space Debris Collision" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Space Debris Collision
                current_time += datetime.timedelta(hours=2)
            elif "Solar Flare Activity" in random_event:
                #time.sleep(2)  # Sleep for 2 hours for Solar Flare Activity
                current_time += datetime.timedelta(hours=2)
            elif "Bird Strike (launch)" in random_event:
                #time.sleep(4)  # Sleep for 4 hours for Bird Strike (launch)
                current_time += datetime.timedelta(hours=4)
            elif "UFO Encounter" in random_event:
                #time.sleep(4)  # Sleep for 4 hours for UFO Encounter
                current_time += datetime.timedelta(hours=4)
            elif "ISS Docking Delay" in random_event:
                ##time.sleep(1)  # Sleep for 1 hour for ISS Docking Delay
                current_time += datetime.timedelta(hours=1)
            # For the "No Events!" case
            elif "No Events!" in random_event:
                #time.sleep(0)  # Default sleep time for no events

                print('Arrived Next Location', current_time.strftime('%m/%d/%Y %I:%M %p'))
            if hours_traveled == 24:
                #time.sleep(24 / 2)
                current_time += datetime.timedelta(hours=24 / 2)  # Add half of travel time
            elif hours_traveled == 384:
                #time.sleep(384 / 2)
                current_time += datetime.timedelta(hours=384 / 2)  # Add half of travel time
            elif hours_traveled == 48:
                #time.sleep(48 / 2)
                current_time += datetime.timedelta(hours=48 / 2)  # Add half of travel time
            elif hours_traveled == 72:
                #time.sleep(72 / 2)
                current_time += datetime.timedelta(hours=72 / 2)  # Add half of travel time
            elif hours_traveled == 840:
                #time.sleep(840 / 2)
                current_time += datetime.timedelta(hours=840 / 2)  # Add half of travel time
            elif hours_traveled == 1152:
                #time.sleep(1152 / 2)
                current_time += datetime.timedelta(hours=1152 / 2)  # Add half of travel time
            elif hours_traveled == 912:
                #time.sleep(912 / 2)
                current_time += datetime.timedelta(hours=912 / 2)  # Add half of travel time
            elif hours_traveled == 360:
                #time.sleep(360 / 2)
                current_time += datetime.timedelta(hours=360 / 2)  # Add half of travel time
            elif hours_traveled == 408:
                #time.sleep(408 / 2)
                current_time += datetime.timedelta(hours=408 / 2)  # Add half of travel time
            elif hours_traveled == 216:
                #time.sleep(216 / 2)
                current_time += datetime.timedelta(hours=216 / 2)  # Add half of travel time
            elif hours_traveled == 96:
                #time.sleep(96 / 2)
                current_time += datetime.timedelta(hours=96 / 2)  # Add half of travel time
            elif hours_traveled == 120:
                #time.sleep(120 / 2)
                current_time += datetime.timedelta(hours=120 / 2)  # Add half of travel time
            elif hours_traveled == 192:
                #time.sleep(192 / 2)
                current_time += datetime.timedelta(hours=192 / 2)  # Add half of travel time
            elif hours_traveled == 456:
                #time.sleep(456 / 2)
                current_time += datetime.timedelta(hours=456 / 2)  # Add half of travel time
            elif hours_traveled == 744:
                #time.sleep(744 / 2)
                current_time += datetime.timedelta(hours=744 / 2)  # Add half of travel time
            elif hours_traveled == 240:
                #time.sleep(240 / 2)
                current_time += datetime.timedelta(hours=240 / 2)  # Add half of travel time

            destination_arrival_timestamp = current_time
            print('Arrived at Destination Location', current_time.strftime('%m/%d/%Y %I:%M %p'))
            #time.sleep(2)
            current_time += datetime.timedelta(hours=2)  # Add 2 hours

            unloaded_transport_timestamp = current_time
            print('Unloaded from Transport', current_time.strftime('%m/%d/%Y %I:%M %p'))
            #time.sleep(2)
            current_time += datetime.timedelta(hours=2)  # Add 2 hours

            unloaded_container_timestamp = current_time
            print('Unloaded from Container', current_time.strftime('%m/%d/%Y %I:%M %p'))
            #time.sleep(5)
            current_time += datetime.timedelta(hours=5)  # Add 5 hours

            picked_up_destination_timestamp = current_time
            print('Picked up at Destination', current_time.strftime('%m/%d/%Y %I:%M %p'))

            # For demonstration purposes, let's return a simple JSON response
            response_data = {'Arrival': origin_timestamp,'loaded': container_loaded_timestamp,'enroute':enroute_timestamp,
                             'unloadedTransport': unloaded_transport_timestamp,'unloadedContainer':unloaded_container_timestamp,
                             'pickup':picked_up_destination_timestamp}

            return jsonify(response_data)


def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'  # Adjust the origin based on your React app's location
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
# app.after_request(add_cors_headers)

#
# @app.route('/start-simulation', methods=['GET'])
# def start_simulation():
#
#     return jsonify({'status': 'success', 'message': 'Simulation started successfully'})


@app.route('/simulate-transportation', methods=['POST'])
def simulate_transportation():
    # Assuming the data is sent in JSON format in the request body
    request_data = request.get_json()

    origin = request_data.get('firstThreeLettersSlice')
    print(origin)
    destination = request_data.get('firstThreeLettersSlice_1')
    service_class = request_data.get('classOfService')
    print(service_class)
    # origin = request_data.get('origin')
    # destination = request_data.get('destination')
    # service_class = request_data.get('service_class')
    response = generate_data(origin, destination, service_class)
    # For demonstration purposes, let's return a simple JSON response
    # response_data = {"message": "Data generated successfully!"}
    print(response)
    return response


app.after_request(add_cors_headers)
if __name__ == '__main__':
    app.run(debug=True)
