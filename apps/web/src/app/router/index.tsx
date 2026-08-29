import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from '../../features/auth/pages/LoginPage';
import RegisterPage from '../../features/auth/pages/RegisterPage';
import { getCurrentUser, logout } from '../../features/auth/api/authService';

const Dashboard = () => {
  const user = getCurrentUser();
  if (!user) return <Navigate to="/login" />;
  
  return (
    <div style={{ textAlign: 'center', padding: '2rem' }}>
      <h1>Welcome, {user.name}!</h1>
      <p>You have successfully logged in.</p>
      <button 
        onClick={() => { logout(); window.location.reload(); }}
        style={{
          marginTop: '1rem',
          padding: '0.5rem 1rem',
          backgroundColor: '#ef4444',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer'
        }}
      >
        Logout
      </button>
    </div>
  );
};

export const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/" element={<Dashboard />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </BrowserRouter>
  );
};
