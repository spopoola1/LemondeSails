import React, { useEffect, useState } from 'react';
import Card from '../components/UI/Card';
import classes from './SimulationDetails.module.css';
import godzillaGif from 'C:/Users/konco/Desktop/Sails Repo/lemondesails/sam-ui-test/src/godzilla.gif'; // Import your Godzilla GIF

function SimulationDetails() {
  const [showIntermodalDetails, setShowIntermodalDetails] = useState(false);

  return (
    <Card>
      <div className={classes.cardHeader}>
        <h2>Shipment Details</h2>
      </div>
      <div className={classes.content}>
        <div className={classes.shipmentInfo}>
          <ul className={classes.shipmentList}>
            <li>Origin: ATL Atlanta</li>
            <li>Destination: CLT Charlotte</li>
            <li>Class: Express</li>
            <li>Cost: 693.1</li>
            <li>Estimated Travel Time: 24 hours</li>
          </ul>
        </div>
        <div className={classes.divider}></div>
        <div className={classes.shipmentUpdates}>
          <ShipmentUpdates setShowIntermodalDetails={setShowIntermodalDetails} />
        </div>
        <div className={classes.divider}></div>
        {showIntermodalDetails && (
          <div className={classes.intermodalDetails}>
            <IntermodalDetails />
          </div>
        )}
      </div>
    </Card>
  );
}

function ShipmentUpdates({ setShowIntermodalDetails }) {
  const [shipmentItems, setShipmentItems] = useState([]);

  useEffect(() => {
    const items = [
      'Received at Origin Location 12/04/2023 07:07 AM',
      'Loaded to Container 12/04/2023 08:07 AM',
      'Loaded onto Transport 12/04/2023 09:07 PM',
      'Enroute to Next Location 12/04/2023 11:07 AM',
      'Event - Godzilla, Response: Rerouting to safety, expected to add approx. 24 hours (Probability: 17.5%)',
      'Truck is back on route and Continuing to next Location 12/05/2023 11:07 AM',
      'Arrived at Destination Location 12/05/2023 02:07 PM',
      'Unloaded from Transport 12/05/2023 04:07 PM',
      'Unloaded from Container 12/05/2023 05:07 PM',
      'Picked up at Destination 12/05/2023 08:07 PM',
    ];

    const displayOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    const timeDelays = [1000, 2000, 3000, 5000, 7000, 9000, 12000, 14000, 15000, 18000];

    const timeoutIds = displayOrder.map((orderIndex, index) =>
      setTimeout(() => {
        setShipmentItems((prevItems) => [...prevItems, items[orderIndex]]);
        if (index === displayOrder.length - 1) {
          setShowIntermodalDetails(true);
        }
      }, timeDelays[index])
    );

    return () => {
      timeoutIds.forEach((timeoutId) => clearTimeout(timeoutId));
    };
  }, [setShowIntermodalDetails]);

  return (
    <div>
      <ul className={classes.shipmentList}>
        {shipmentItems.map((item, index) => (
          <li key={index}>
            {item.includes('Godzilla') ? (
              <>
                {item}
                <img src={godzillaGif} alt="Godzilla GIF" className={classes.godzillaGif} />
              </>
            ) : (
              item
            )}
          </li>
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
        <li>Intermodal Mix: Truck</li>
        <li>Transfer Points: 0</li>
        <li>Travelled Hours: 49</li>
      </ul>
    </div>
  );
}

export default SimulationDetails;
