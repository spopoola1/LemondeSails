import React, { useState, useEffect } from 'react';
import Card from '../components/UI/Card';
import classes from './SimulationDetails.module.css';

function SimulationDetails() {
  return (
    <Card>
      <div className={classes.cardHeader}>
        <h2>Shipment Details</h2>
      </div>
      <div className={classes.content}>
        <div className={classes.shipmentInfo}>
          <ul className={classes.shipmentList}>
            <li>Class: Premium</li>
            <li>Cost: 2594</li>
            <li>Origin: LAX Los Angeles</li>
            <li>Destination: SEA Seattle</li>
          </ul>
        </div>
        <div className={classes.divider}></div>
        <div className={classes.shipmentUpdates}>
          <ShipmentUpdates />
        </div>
        <div className={classes.divider}></div>
        <div className={classes.intermodalDetails}>
          <IntermodalDetails />
        </div>
      </div>
    </Card>
  );
}

function ShipmentUpdates() {
  const [updates, setUpdates] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/simulation/updates');
        const data = await response.json();
        setUpdates(data.shipment_updates || []);
      } catch (error) {
        console.error('Error fetching shipment updates:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <ul className={classes.shipmentList}>
        {updates.map((update, index) => (
          <li key={index}>{update}</li>
        ))}
      </ul>
    </div>
  );
}

function IntermodalDetails() {
  return (
    <div>
      <h3>Intermodal Details</h3>
      <ul className={classes.shipmentList}>
        <li>Intermodal Mix: Truck, Plane</li>
        <li>Transfer Points: 2</li>
        <li>Travelled Hours: 73</li>
        <li>Events Affecting Shipment: Hailstorm</li>
      </ul>
    </div>
  );
}

export default SimulationDetails;