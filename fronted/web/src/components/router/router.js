import {BrowserRouter, Route, Switch} from 'react-router-dom';
import React, {Component} from 'react';
import Login from '../user/login';
import Register from '../user/register';

export default class Router extends Component {
	render() {
		return (
		    <BrowserRouter>
			    <Switch>
				    <Route exact path="/login" component={Login} />
					<Route exact path="/register" component={Register}/>
				</Switch>
			</BrowserRouter>
		)
	}
}