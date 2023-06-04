import React, {Component} from "react";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import LoginPage from "./LoginPage";
import HomePage from "./HomePage";
import Nav from "./Nav";
import {AuthProvider} from "../contexts/AuthContext";
import ProtectedRoute, { UnprotectedRoute } from "./ProtectedRoute";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import LoginForm from "./LoginForm";
import SignupForm from "./SignupForm";

export default function Home() {
    const APIUrl = "http://localhost:8000/";
    return (
        <Router>
            <AuthProvider APIUrl={APIUrl}>
                <Nav />
            <Switch>
                <Route exact path='/' component={HomePage}></Route>
                <UnprotectedRoute
                    exact
                    path="/login"
                    redirect="/"
                    component={LoginForm}
                    key="login"
                />
                <UnprotectedRoute
                    exact
                    path="/signup"
                    redirect="/"
                    component={SignupForm}
                    key="signup"
                />

            </Switch>
            </AuthProvider>
        </Router>
    );
}

