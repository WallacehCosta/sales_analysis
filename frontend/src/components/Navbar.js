import React from "react";

const Navbar = () => {
  return (
    <nav className="bg-blue-600 p-4 text-white shadow-lg">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold">Sales Analyzer</h1>
        <div className="flex space-x-4">
          <a href="/" className="hover:text-gray-300">Dashboard</a>
          <a href="/reports" className="hover:text-gray-300">Reports</a>
          <a href="/settings" className="hover:text-gray-300">Settings</a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
