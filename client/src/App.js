import React from 'react';
import Home from "./Home";
import Navbar from "./Navbar";
import Bookmarks from "./Bookmarks";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

const App = () => {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/About" element={<Bookmarks />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
