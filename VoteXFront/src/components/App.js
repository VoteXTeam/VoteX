import React from "react";
import { render } from "react-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

import Home from "./Home";

export default function App() {
        return (
            <div className="App">
                <Home />
            </div>
        )
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

