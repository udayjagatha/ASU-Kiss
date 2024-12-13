import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import StudentPage from "./pages/StudentPage";
import BadgesPage from "./pages/BadgesPage";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/students" element={<StudentPage />} />
        <Route path="/" element={<LoginPage />} /> {/* Default route */}
        <Route path="/badges" element={<BadgesPage />} />
      </Routes>
    </Router>
  );
};

export default App;
