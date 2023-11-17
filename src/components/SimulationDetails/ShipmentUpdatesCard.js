import React from 'react';
import Card from '../UI/Card';
import classes from './ShipmentUpdatesCard.module.css';

function ShipmentUpdatesCard() {
  return (
    <Card>
      <div className={classes.content}>
        <h3>Shipment Updates</h3>
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
    </Card>
  );
}

export default ShipmentUpdatesCard; // Default export
