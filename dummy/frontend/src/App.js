import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/Home'
import JobApplications from './components/JobApplications';  // Import JobApplications component

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/job-applications">Job Applications</Link></li>
            </ul>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/job-applications" element={<JobApplications />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
