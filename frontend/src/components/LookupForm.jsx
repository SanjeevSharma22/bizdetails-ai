import React, { useState } from 'react';
import api from '../services/api.js';
import ResultsTable from './ResultsTable.jsx';

export default function LookupForm() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const search = async (e) => {
    e.preventDefault();
    // TODO: integrate API
    setResults([]);
  };

  return (
    <div className="p-4">
      <form onSubmit={search} className="mb-4">
        <input
          type="text"
          placeholder="Company name or domain"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="border p-2 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2">
          Search
        </button>
      </form>
      <ResultsTable results={results} />
    </div>
  );
}
