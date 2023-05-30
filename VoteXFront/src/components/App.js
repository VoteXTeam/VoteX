import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import LoginPage from "./LoginPage";

export default  class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        //Only one element
        return (
            <div>
                <HomePage />
            </div>
        )
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

