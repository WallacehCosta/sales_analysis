import React from "react";

const Card = ({ title, value, icon }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <div className="flex items-center space-x-4">
        <div className="text-blue-600">{icon}</div>
        <div>
          <h3 className="text-lg font-bold">{title}</h3>
          <p className="text-gray-700">{value}</p>
        </div>
      </div>
    </div>
  );
};

export default Card;
