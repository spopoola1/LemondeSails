import React from 'react';
import { Routes, Route } from 'react-router-dom';
import SimulationDetailsPage from './Pages/SimulationDetails';
import NewSimulationPage from './Pages/NewSimulation';
import SimulationHistoryPage from './Pages/SimulationHistory';
import Layout from './components/layout/Layout';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<NewSimulationPage />} />
        <Route path="/simulation-history" element={<SimulationHistoryPage />} />
        <Route path="/simulation-details" element={<SimulationDetailsPage />} />
      </Routes>
    </Layout>
  );
}

export default App;