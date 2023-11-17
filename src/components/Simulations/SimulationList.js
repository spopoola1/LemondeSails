import SimulationItem from './SimulationItem';
import classes from './simulationlist.module.css';

function SimulationList(props) {
    return (
        <ul className={classes.list}>
            {props.simulations.map((simulation) => (
                <SimulationItem
                    key={simulation.id}
                    id={simulation.id}
                    title={simulation.title}
                    address={simulation.address}
                    description={simulation.description} 
                />
            ))}
        </ul>
    );
}

export default SimulationList;