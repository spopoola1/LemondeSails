import React from 'react';
import Card from '../UI/Card';
import classes from './simulationitem.module.css'

function SimulationItem(props) {
    return (
      <li className={classes.item}>
        <Card>
          <div className={classes.content}>
            <h3>{props.title}</h3>
            <address>{props.address}</address>
            <p>{props.description}</p>
          </div>
          <div className={classes.actions}>
            <button>View Simulation</button>
          </div>
        </Card>
      </li>
    );
  }

export default SimulationItem;