import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./styles/global.css";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import SalesAnalysis from "./pages/SalesAnalysis";
import Reports from "./pages/Reports";
import Settings from "./pages/Settings";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

const App = () => {
  return (
    <Router>
      <Routes>
        {/* Rota pública (login) */}
        <Route path="/" element={<Login />} />

        {/* Rotas privadas (protegidas por autenticação) */}
        <Route
          path="/dashboard"
          element={
            <>
              <Navbar />
              <Sidebar />
              <Dashboard />
            </>
          }
        />
        <Route
          path="/sales-analysis"
          element={
            <>
              <Navbar />
              <Sidebar />
              <SalesAnalysis />
            </>
          }
        />
        <Route
          path="/reports"
          element={
            <>
              <Navbar />
              <Sidebar />
              <Reports />
            </>
          }
        />
        <Route
          path="/settings"
          element={
            <>
              <Navbar />
              <Sidebar />
              <Settings />
            </>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;
