import Alert from 'react-s-alert';

export default function show_error(message) {
	Alert.error(message, {
		position: 'top-right',
		effect: 'slide',
	});
}