import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Chart from "../components/Chart";
import Card from "../components/Card";

const Dashboard = () => {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1">
        <Navbar />
        <div className="p-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <Card title="Total Sales" value="$12,345" icon="💰" />
            <Card title="Total Orders" value="1,234" icon="📦" />
            <Card title="Customers" value="567" icon="👤" />
          </div>
          <Chart />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
