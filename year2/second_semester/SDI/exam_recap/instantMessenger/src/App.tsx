import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import * as React from "react";
//import "./App.css";
import { FirstTable } from "./firstTable";
import { MCP } from "./MCP";

function App() {
  return (
    <React.Fragment>
      <Router>
        <Routes>
          <Route path="/" element={<FirstTable />} />
        </Routes>
        <Routes>
          <Route path="/channels/:GUID" element={<MCP />} />
        </Routes>
      </Router>
    </React.Fragment>
  );
}

export default App;
