import React, { useState } from 'react';
import axios from 'axios';

function CreateJob() {
  const [jobData, setJobData] = useState({
    job_id: 0, // Initialize job_id
    job_name: '',
    job_role: '',
    job_description: '',
    last_date: '',
    questions: [{ question_text: '' }] // Start with one question field
  });

  const handleInputChange = (e) => {
    setJobData({
      ...jobData,
      [e.target.name]: e.target.value,
    });
  };

  const handleQuestionChange = (index, event) => {
    const newQuestions = [...jobData.questions];
    newQuestions[index].question_text = event.target.value;
    setJobData({ ...jobData, questions: newQuestions });
  };

  const addQuestionField = () => {
    setJobData({
      ...jobData,
      questions: [...jobData.questions, { question_text: '' }],
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Check if there are any empty question texts
    const hasEmptyQuestions = jobData.questions.some(q => q.question_text.trim() === '');
    if (hasEmptyQuestions) {
        alert('Please fill in all question fields.');
        return;
    }

    // Log the jobData to see what is being sent
    console.log('Submitting Job Data:', jobData);

    axios.post('http://127.0.0.1:8000/api/create_job/', jobData, {
        headers: {
            'Content-Type': 'application/json', // Specify content type
        },
    })
    .then(response => {
        alert('Job created successfully!');
        setJobData({
            job_id: 0, // Reset job_id if needed
            job_name: '',
            job_role: '',
            job_description: '',
            last_date: '',
            questions: [{ question_text: '' }]
        });
    })
    .catch(error => {
        alert('Failed to create job. Please try again.');
        console.error('Error details:', error.response ? error.response.data : error.message);
    });
  };

  return (
    <div>
      <h2>Create Job</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Job ID:</label>
          <input
            type="number"
            name="job_id"
            value={jobData.job_id}
            onChange={handleInputChange}
            required
          />
        </div>

        <div>
          <label>Job Name:</label>
          <input
            type="text"
            name="job_name"
            value={jobData.job_name}
            onChange={handleInputChange}
            required
          />
        </div>

        <div>
          <label>Job Role:</label>
          <input
            type="text"
            name="job_role"
            value={jobData.job_role}
            onChange={handleInputChange}
            required
          />
        </div>

        <div>
          <label>Job Description:</label>
          <textarea
            name="job_description"
            value={jobData.job_description}
            onChange={handleInputChange}
            required
          />
        </div>

        <div>
          <label>Last Date:</label>
          <input
            type="date"
            name="last_date"
            value={jobData.last_date}
            onChange={handleInputChange}
            required
          />
        </div>

        <div>
          <h4>Questions</h4>
          {jobData.questions.map((question, index) => (
            <div key={index}>
              <input
                type="text"
                value={question.question_text}
                onChange={(e) => handleQuestionChange(index, e)}
                placeholder={`Question ${index + 1}`}
                required
              />
            </div>
          ))}
          <button type="button" onClick={addQuestionField}>
            Add Another Question
          </button>
        </div>

        <button type="submit">Create Job</button>
      </form>
    </div>
  );
}

export default CreateJob;
