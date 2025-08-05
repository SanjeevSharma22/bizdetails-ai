import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginForm from './components/LoginForm.jsx';
import Dashboard from './components/Dashboard.jsx';
import LookupForm from './components/LookupForm.jsx';
import BulkUpload from './components/BulkUpload.jsx';
import AdminSettings from './components/AdminSettings.jsx';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/lookup" element={<LookupForm />} />
        <Route path="/upload" element={<BulkUpload />} />
        <Route path="/admin" element={<AdminSettings />} />
      </Routes>
    </Router>
  );
}
