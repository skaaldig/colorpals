import React, { Component } from 'react';
import './App.css';

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import Colors from "./Component/Colors/index";

class App extends Component {
  render() {
    return (
      <Router>
        <Route path="/" exact component={Colors} />
    </Router>
    );
  }
}

export default App;