import SimulationList from "../components/Simulations/SimulationList";

const DUMMY_DATA = [
    {
      id: 's1',
      title: 'ATL: Atlanta TO CLT: Charlotte',
      address: 'Class: Express, Mode: Truck',
      description:
        'Delivery Date: 12/05/23, Events: Godzilla, Days of Travel: 2, Estimated Delivery Time: 48 Hours',
    },
];

//function for displaying data from simulationList.js to the webpage
function SimulationHistoryPage() {
    return (
      <section>
        <SimulationList simulations={DUMMY_DATA} />
      </section>
    );
  }

export default SimulationHistoryPage;