import React from 'react';
import { Link } from 'react-router-dom'; // Import Link from React Router
import Card from '../UI/Card';
import classes from './simulationitem.module.css';

// Function for displaying previous simulations
function SimulationItem(props) {
  const viewSimulationHandler = () => {
    // Handle the logic to navigate to the simulation details page
    // You can use react-router-dom's history or any other navigation method
  };

  return (
    <li className={classes.item}>
      {/* Card component used to wrap previous simulation details into a container for styling */}
      <Card>
        {/* Displays data from simulationList.js, also allows for styling */}
        <div className={classes.content}>
          <h3>{props.title}</h3>
          <address>{props.address}</address>
          <p>{props.description}</p>
        </div>
        <div className={classes.actions}>
          {/* Use Link to navigate to the simulation details page */}
          <Link to="/simulation-details">
            <button onClick={viewSimulationHandler}>View Simulation</button>
          </Link>
        </div>
      </Card>
    </li>
  );
}

export default SimulationItem;