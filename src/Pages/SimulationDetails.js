import React from 'react';
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
  return (
    <div>
      <ul className={classes.shipmentList}>
        <li>Received at Origin Location</li>
        <li>Loaded on container</li>
        <li>Loaded on Transport</li>
        <li>En-route to Next Location</li>
        <li>Route Delay: 1 hour delay, Heavy Hailstorm</li>
        <li>Truck is back on route and Continuing to next Location</li>
        <li>Arrived Next Location</li>
        <li>Arrived at Destination Location</li>
        <li>Unloaded from Transport</li>
        <li>Unloaded from Container</li>
        <li>Picked up at Destination</li>
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
