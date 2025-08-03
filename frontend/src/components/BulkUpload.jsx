import React, { useState } from 'react';
import api from '../services/api.js';

export default function BulkUpload() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
    // TODO: send to API
  };

  return (
    <div className="p-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 ml-2">
        Upload
      </button>
    </div>
  );
}
