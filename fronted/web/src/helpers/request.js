export default class Request {
	post(path, body) {
		return new Promise((resolve, reject) => {
			fetch(('http://127.0.0.1:8088/' + path),
			    {
					method: 'POST',
					credentials: 'same-origin',
					headers: {'Content-Type': 'application/json'},
					body: JSON.stringify(body),
				}).then(response => resolve(response.json())).catch(error => reject(error))
		})
	}
}