import { Link } from "react-router-dom";

import classes from './MainNavigation.module.css'

function MainNavigation() {
    return (
    <header className={classes.header}>
        <div className={classes.logo}>Welcome To LeMonde Sails</div>
        <nav>
            <ul>
                <li>
                    <Link to = '/'>New Simulation</Link>
                </li>
                <li>
                    <Link to = '/simulation-details'>Simulation Details</Link>
                </li>
                <li>
                    <Link to = '/simulation-history'>Simulation History</Link>
                </li>
            </ul>
        </nav>
    </header>
    );
}

export default MainNavigation;