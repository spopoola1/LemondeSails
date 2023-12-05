import React, { useState } from 'react';
import Card from "../UI/Card";
import classes from './SimulationForm.module.css';
import { useNavigate } from 'react-router-dom';
import routesData from '../../routesData';

function NewSimulationForm() {
  const [selectedOrigin, setSelectedOrigin] = useState('');
  const [selectedDestination, setSelectedDestination] = useState('');
  const [selectedClassOfService, setSelectedClassOfService] = useState('');

  const originOptions = [ null, "ABZ",
  "ANC",
  "ATL",
  "BOM",
  "BWN",
  "CCU",
  "CHS",
  "CLT",
  "DEL",
  "DFW",
  "EDI",
  "HYD",
  "IAH",
  "ISS",
  "KUL",
  "LAX",
  "MEL",
  "MEX",
  "MSY",
  "NSP",
  "ORD",
  "PNY",
  "SAN",
  "SAT",
  "SCL",
  "SEA",
  "SHL",
  "SIN",
  "STL",
  "SYD",
  "ZAL"];
  const destinationOptions = [ null, "ABZ",
  "ANC",
  "ATL",
  "BOM",
  "BWN",
  "CCU",
  "CHS",
  "CLT",
  "DEL",
  "DFW",
  "EDI",
  "HYD",
  "IAH",
  "ISS",
  "KUL",
  "LAX",
  "MEL",
  "MEX",
  "MSY",
  "NSP",
  "ORD",
  "PNY",
  "SAN",
  "SAT",
  "SCL",
  "SEA",
  "SHL",
  "SIN",
  "STL",
  "SYD",
  "ZAL"];
  const classOfServiceOptions = [null, "Standard", "Express", "Premium"];
  const navigate = useNavigate();

  const submitHandler = (event) => {
    event.preventDefault();

    // Validate user input against the hardcoded routes Data
    const isValidSelection = routesData.some(route =>
      route.origin === selectedOrigin &&
      route.destination === selectedDestination &&
      route.classOfService === selectedClassOfService
    );

    if (!isValidSelection) {
      alert('There are no routes for the selections you have made.');
      return;
    }

    navigate('/simulation-details');
  };

  return (
    <Card>
      <h1>Input A Shipment</h1>
      <form className={classes.form} onSubmit={submitHandler}>
        <div className={classes.control}>
          <label htmlFor='origin'>Origin</label>
          <select
            id="origin"
            value={selectedOrigin}
            onChange={(e) => setSelectedOrigin(e.target.value)}
            required
          >
            {originOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='destination'>Destination</label>
          <select
            id="destination"
            value={selectedDestination}
            onChange={(e) => setSelectedDestination(e.target.value)}
            required
          >
            {destinationOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='classOfService'>Class Of Service</label>
          <select
            id="classOfService"
            value={selectedClassOfService}
            onChange={(e) => setSelectedClassOfService(e.target.value)}
            required
          >
            {classOfServiceOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='deliveryDate'>Delivery Date</label>
          <input type='date' required id='deliveryDate' />
        </div>
        <div className={classes.actions}>
          <button type='submit'>Start Simulation</button>
        </div>
      </form>
    </Card>
  );
}

export default NewSimulationForm;