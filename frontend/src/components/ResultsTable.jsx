import React from 'react';

export default function ResultsTable({ results }) {
  if (!results.length) return <p>No results</p>;

  return (
    <table className="min-w-full border">
      <thead>
        <tr>
          <th className="border px-2">Name</th>
          <th className="border px-2">Domain</th>
        </tr>
      </thead>
      <tbody>
        {results.map((r) => (
          <tr key={r.id}>
            <td className="border px-2">{r.name}</td>
            <td className="border px-2">{r.domain}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
