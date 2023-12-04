import SimulationList from "../components/Simulations/SimulationList";

const DUMMY_DATA = [
    {
      id: 's1',
      title: 'BWN: SpaceX Launch City TO ISS: International Space Station',
      address: 'Class: Premium, Mode: Falcon',
      description:
        'Delivery Date: 10/25/23, Events: Strong Winds, Days of Travel: 4, Estimated Delivery Time: 86 Hours',
    },
    {
      id: 's2',
      title: 'BOM: Mumbai to HYD: Hyderabad',
      address: 'Class: Express, Mode: Train',
      description:
        'Delivery Date: 10/20/23, Events: Heavy Snow, Days of Travel: 2, Estimated Delivery Time: 48 Hours',
    },
    {
      id: 's3',
      title: 'CLT: Mumbai to LAX: Hyderabad',
      address: 'Class: Premium, Mode: Plane',
      description:
        'Delivery Date: 10/20/23, Events: Thunderstorm, Days of Travel: 1 + 1, Estimated Delivery Time: 48 Hours',
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