import React from 'react';
import Card from '../UI/Card';
import classes from './IntermodalDetailsCard.module.css';

function IntermodalDetailsCard() {
  return (
    <Card>
      <div className={classes.content}>
        <h3>Intermodal Mix</h3>
        <p></p>
      </div>
      <div className={classes.content}>
        <h3>Transfer Points</h3>
        <p>2</p>
      </div>
      <div className={classes.content}>
        <h3>Travelled Hours</h3>
        <p>73</p>
      </div>
    </Card>
  );
}

export default IntermodalDetailsCard; // Default export
