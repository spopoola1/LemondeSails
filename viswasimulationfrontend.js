import Card from "../UI/Card";
import classes from './SimulationForm.module.css';
import { useNavigate } from 'react-router-dom';
import React, { useState } from 'react';


function NewSimulationForm() {
  const originOptions = [ null, "ABZ: Aberdeen",
  "ANC: Anchorage",
  "ATL: Atlanta",
  "BOM: Mumbai",
  "BWN: Brownsville",
  "CCU: Kolkata",
  "CHS: Charleston",
  "CLT: Charlotte",
  "DEL: Delhi",
  "DFW: Dallas",
  "EDI: Edinburgh",
  "HYD: Hyderabad",
  "IAH: Houston",
  "ISS: International Space Station",
  "KUL: Kuala Lumpur",
  "LAX: Los Angeles",
  "MEL: Melbourne",
  "MEX: Mexico City",
  "MSY: New Orleans",
  "NSP: McMurdo Station",
  "ORD: Chicago",
  "PNY: Pondicherry",
  "SAN: San Diego",
  "SCL: Santiago",
  "SHL: Shimla",
  "SIN: Singapore",
  "STL: St Louis",
  "SYD/: Sydney",
  "ZAL: Valdivia"];

  const destinationOptions = [ null, "ABZ: Aberdeen",
  "ANC: Anchorage",
  "ATL: Atlanta",
  "BOM: Mumbai",
  "BWN: Brownsville",
  "CCU: Kolkata",
  "CHS: Charleston",
  "CLT: Charlotte",
  "DEL: Delhi",
  "DFW: Dallas",
  "EDI: Edinburgh",
  "HYD: Hyderabad",
  "IAH: Houston",
  "ISS: International Space Station",
  "KUL: Kuala Lumpur",
  "LAX: Los Angeles",
  "MEL: Melbourne",
  "MEX: Mexico City",
  "MSY: New Orleans",
  "NSP: McMurdo Station",
  "ORD: Chicago",
  "PNY: Pondicherry",
  "SAN: San Diego",
  "SCL: Santiago",
  "SHL: Shimla",
  "SIN: Singapore",
  "STL: St Louis",
  "SYD/: Sydney",
  "ZAL: Valdivia"];
  
  const classOfServiceOptions = [null, "Standard", "Express", "Premium"];

  const navigate = useNavigate();
  const [simulationResult, setSimulationResult] = useState(0);
  const [apiResult, setApiResult] = useState('');



  const postSubmitHandler = async (event) => {

  
    event.preventDefault();

    const origin = document.getElementById('origin').value;
    const firstThreeLettersSlice = origin.slice(0, 3);
    const destination = document.getElementById('destination').value;
    const firstThreeLettersSlice_1 = destination.slice(0, 3);
    const classOfService = document.getElementById('classOfService').value;
    // const deliveryDate = document.getElementById('deliveryDate').value;
    // const responseData = ''
  
    const userInputs = {
      firstThreeLettersSlice,
      firstThreeLettersSlice_1,
      classOfService,
      // deliveryDate,
    };
        // Navigate to the Simulation Details page
        //navigate('/simulation-details',{a:apiResult.Unloaded});
    try {
      const response = await fetch('http://127.0.0.1:5000/simulate-transportation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userInputs),
      });
  
      const responseData = await response.json();

      console.log(responseData)
  
      // Set the simulationResult state variable to the response from the backend
      setSimulationResult(!simulationResult);
      setApiResult(responseData);
      console.log(apiResult);

    } catch (error) {
      console.error('Error:', error);
    }
  };  

  return (
    <Card>
      <h1>Create New Simulation</h1>
      <form className={classes.form} onSubmit={postSubmitHandler}>
        <div className={classes.control}>
          <label htmlFor='origin'>Origin</label>
          <select id="origin" required>
            {originOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='destination'>Destination</label>
          <select id="destination" required>
            {destinationOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='classOfService'>Class Of Service</label>
          <select id="classOfService" required>
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
        {/* <div className={classes.control}>
          <h2>Simulation Result</h2>
          <p>{responseData}</p>
        </div> */}
      </form>
      {simulationResult && (
        <div className={classes.result}>
          <h2>Simulation Result</h2>
          <p> Loaded in Container: {apiResult.loaded}</p>
          <p> Arrived at Location: {apiResult.Arrival}</p>
          <p> Destination Arrival: {apiResult.enroute}</p>
          <p> Unloaded from Transport: {apiResult.unloadedTransport}</p>
          <p> Unloaded from Container: {apiResult.unloadedContainer}</p>
          <p> Destination Arrival: {apiResult.pickup}</p>
          
        </div>
      )}
    </Card>
  );
}

export default NewSimulationForm;






















