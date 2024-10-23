// JobList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function JobList() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/list_jobs/')
      .then(response => {
        setJobs(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError('Error fetching jobs');
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h2>Job List</h2>
      {jobs.length > 0 ? (
        <ul>
          {jobs.map(job => (
            <li key={job.job_id}>
              <h3>{job.job_name} ({job.job_role})</h3>
              <p>{job.job_description}</p>
              <p>Last Date to Apply: {job.last_date}</p>
              <h4>Questions:</h4>
              <ul>
                {job.questions.map((question, index) => (
                  <li key={index}>{question.question_text}</li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      ) : (
        <p>No jobs found.</p>
      )}
    </div>
  );
}

export default JobList;
