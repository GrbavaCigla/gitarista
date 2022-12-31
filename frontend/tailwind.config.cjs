const config = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			fontFamily: {
				logo: 'Pacifico'
			}
		}
	},
	plugins: [require('daisyui')]
};

module.exports = config;
