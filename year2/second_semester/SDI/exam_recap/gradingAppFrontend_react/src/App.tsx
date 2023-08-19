//import { useState } from "react";

import "./App.css";
import * as React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { FirstTable } from "./firstTable";
import { Create } from "./create";
import { EDP } from "./examinationDashboardPage";
import { EGP } from "./examinerGradebookPage";

function App() {
  return (
    <React.Fragment>
      <Router>
        <Routes>
          <Route path="/" element={<FirstTable />} />
          <Route path="/examination/create" element={<Create />} />
          <Route
            path="/examination/dashboard/:titleGUID/:titleId"
            element={<EDP />}
          />
          <Route
            path="/examination/session/:titleGUID/grading/:examinerGUID"
            element={<EGP />}
          />
        </Routes>
      </Router>
    </React.Fragment>
  );
}

export default App;
