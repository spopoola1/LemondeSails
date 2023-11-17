import React from 'react';
import NewSimulationForm from '../components/Simulations/SimulationForm';
import { useNavigate } from 'react-router-dom'; // Import the useNavigate hook

function NewSimulationPage() {
  const navigate = useNavigate();

  const submitHandler = (event) => {
    event.preventDefault();

    // Perform your form validations here
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
