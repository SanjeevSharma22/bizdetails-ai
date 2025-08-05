import React from 'react';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  return (
    <div className="p-4">
      <h1 className="text-xl mb-4">Dashboard</h1>
      <nav className="space-x-4">
        <Link to="/lookup" className="text-blue-500">Lookup</Link>
        <Link to="/upload" className="text-blue-500">Bulk Upload</Link>
        <Link to="/admin" className="text-blue-500">Admin</Link>
      </nav>
    </div>
  );
}
