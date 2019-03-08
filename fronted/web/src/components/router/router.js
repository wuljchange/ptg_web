import {BrowserRouter, Route, Switch} from 'react-router-dom';
import React, {Component} from 'react';
import Login from '../user/login';

export default class Router extends Component {
	render() {
		return (
		    <BrowserRouter>
			    <Switch>
				    <Route exact path="/login" component={Login} />
				</Switch>
			</BrowserRouter>
		)
	}
}