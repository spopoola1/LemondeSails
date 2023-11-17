import { useState } from "react";
import Card from "../UI/Card";
import classes from './SimulationForm.module.css';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

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

  const [formData, setFormData] = useState({
    origin: '',
    destination: '',
    classOfService: '',
    deliveryDate: ''
  })

  const handleInput = (event) => {
    setFormData({...formData, [event.target.id]: event.target.value})
  }

  const submitHandler = (event) => {
    event.preventDefault();
    console.log(formData)
    // Post request to backend
    axios.post('http://127.0.0.1:5000/userInput', {formData}).then(
      res => console.log(res)
    ).catch(
      err => console.log(err)
    )
    // If validations are successful, navigate to the Simulation Details page
    navigate('/simulation-details');
  };

  return (
    <Card>
      <h1>Create New Simulation</h1>
      <form className={classes.form} onSubmit={submitHandler}>
        <div className={classes.control}>
          <label htmlFor='origin'>Origin</label>
          <select id="origin" required onChange={handleInput}>
            {originOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='destination'>Destination</label>
          <select id="destination" required onChange={handleInput}>
            {destinationOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='classOfService'>Class Of Service</label>
          <select id="classOfService" required onChange={handleInput}>
            {classOfServiceOptions.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className={classes.control}>
          <label htmlFor='deliveryDate'>Delivery Date</label>
          <input type='date' required id='deliveryDate' onChange={handleInput} />
        </div>
        <div className={classes.actions}>
          <button type='submit'>Start Simulation</button>
        </div>
      </form>
    </Card>
  );
}

export default NewSimulationForm;