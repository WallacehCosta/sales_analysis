import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Chart from "../components/Chart";

const SalesAnalysis = () => {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Navbar />
        <div className="p-6">
          <h2 className="text-2xl font-bold mb-6">Sales Analysis</h2>
          <Chart />
        </div>
      </div>
    </div>
  );
};

export default SalesAnalysis;
