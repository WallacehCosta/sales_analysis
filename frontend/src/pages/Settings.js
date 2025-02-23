import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

const Settings = () => {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Navbar />
        <div className="p-6">
          <h2 className="text-2xl font-bold mb-6">Settings</h2>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <p>Configurações serão exibidas aqui.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Settings;
