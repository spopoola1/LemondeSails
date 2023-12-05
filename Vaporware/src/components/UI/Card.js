import classes from './Card.module.css';

//Component for Card container
function Card(props) {
  return <div className={classes.card}>{props.children}</div>;
}

export default Card;