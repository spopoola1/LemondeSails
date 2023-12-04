import React from 'react';
import NewSimulationForm from '../components/Simulations/SimulationForm';
import { useNavigate } from 'react-router-dom';

//function for creating a new simulation
function NewSimulationPage() {
  const navigate = useNavigate();


  //function for handling form submissions
  const submitHandler = (event) => {
    event.preventDefault();


    // If validations are successful, navigate to the Simulation Details page
    navigate('/simulation-details');
  };

  return (
    <section>
      <NewSimulationForm onSubmit={submitHandler} />
    </section>
  );
}

export default NewSimulationPage;