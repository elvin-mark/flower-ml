import React from "react";
import {
  BarChart,
  CartesianGrid,
  Tooltip,
  Legend,
  Bar,
  XAxis,
  YAxis,
} from "recharts";

function Guess({ data }) {
  return (
    <div>
      <BarChart
        data={data}
        width={500}
        height={500}
        layout="vertical"
        margin={{ left: 80 }}
      >
        <Bar dataKey="prob" fill="#aa2200"></Bar>
        <CartesianGrid strokeDasharray="3 3"></CartesianGrid>
        <XAxis type="number"></XAxis>
        <YAxis dataKey="name" type="category"></YAxis>
        <Legend></Legend>
      </BarChart>
    </div>
  );
}

export default Guess;
