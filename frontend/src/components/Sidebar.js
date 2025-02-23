import React from "react";

const Sidebar = () => {
  return (
    <aside className="bg-gray-800 text-white w-64 min-h-screen p-4">
      <div className="space-y-4">
        <h2 className="text-lg font-bold">Menu</h2>
        <ul className="space-y-2">
          <li>
            <a href="/" className="block p-2 hover:bg-gray-700 rounded">Dashboard</a>
          </li>
          <li>
            <a href="/sales" className="block p-2 hover:bg-gray-700 rounded">Sales</a>
          </li>
          <li>
            <a href="/products" className="block p-2 hover:bg-gray-700 rounded">Products</a>
          </li>
          <li>
            <a href="/analytics" className="block p-2 hover:bg-gray-700 rounded">Analytics</a>
          </li>
        </ul>
      </div>
    </aside>
  );
};

export default Sidebar;
