import React, {Component} from 'react';
import $ from 'jquery';
import Cookies from 'js-cookie';
import Request from '../../helpers/request';
import show_error from '../../helpers/alert';

export default class Login extends Component {
	constructor() {
		super();
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
			    <div class="col-auto">
				    <div class="input-group mb-2">
					    <div class="input-group-prepend">
                            <div class="input-group-text">用户名</div>
                        </div>
                        <input type="text" class="form-control" id="username" placeholder="Username" />
                    </div>
				</div>
				<div class="col-auto">
				    <div class="input-group mb-2">
					    <div class="input-group-prepend">
				            <div class="input-group-text">密码</div>
				        </div>
				        <input type="text" class="form-control" id="password" placeholder="Password" />
				    </div>
				</div>
				<div class="col-auto">
				    <button type="submit" class="btn btn-primary mb-2">登录</button>
				</div>
			</form>
		)
	}
}
