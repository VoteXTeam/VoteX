import React from 'react';

import { Route, Routes } from 'react-router-dom';
import Login from '../components/login/Login';
import Register from '../components/register/Register';
import Candidates from '../components/candidates/Candidates';
import Elections from '../components/elections/Elections';
import Statistics from '../components/statistics/Statistics';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/statistics" element={<Statistics />} />
      <Route path="/election" element={<Candidates />} />
      <Route path="/elections" element={<Elections />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
};

export default AppRoutes;
