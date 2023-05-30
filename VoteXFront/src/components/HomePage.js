import React, { Component } from "react";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import LoginPage from "./LoginPage";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Switch>
                    <Route exact path='/'><p>This is HomePage</p></Route>
                    <Route path='/login' component={LoginPage}></Route>
                </Switch>
            </Router>
        );
    }
}
