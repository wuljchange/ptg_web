import React, {Component} from 'react';
import $ from 'jquery';
import Cookies from 'js-cookie';
import Request from '../../helpers/request';
import show_error from '../../helpers/alert';

export default class Login extends Component {
	constructor(props) {
		super(props);
		this.request = new Request();
		this.make_post = this.make_post.bind(this);
	}
	
	make_post(event) {
		event.preventDefault();
		let body = {username: $("#username").val(), password: $("#password")};
		this.request.post('login', body).then((response) => {
			if (response.hasOwnProperty('alert')) {
				response.alert.map(alert => show_error(alert))
			}
			else {
				Cookies.set('token', response.token, {expires: 1});
				window.location.replace('/home')
			}
		}).catch((error) => {console.log(error);window.location.replace('/home')})
	}
	
	render() {
		return (
			<form onSubmit={event => this.make_post(event)}>
				<div className="form-group">
					<label>用户名</label>
					<input type="text" id="username" className="form-control" placeholder="username" />
				</div>
				<div className="form-group">
					<label>密码</label>
					<input type="password" id="password" className="form-control"/>
				</div>
				<button type="submit" className="btn btn-primary">登录</button>
			</form>
		)
	}
}
