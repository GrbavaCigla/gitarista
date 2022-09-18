const nord = require('tailwind-nord').config.theme.extend.colors();

module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	darkMode: 'media',
	theme: {
		extend: {
			// Aliases
			colors: {
				primary: nord.nord8,
				secondary: nord.nord9,
				tertiary: nord.nord10,

				dark0: nord.nord0, // light: text, dark: background
				dark1: nord.nord1, // dark: card background
				dark2: nord.nord2,
				dark3: nord.nord3,

				light0: nord.nord4,
				light1: nord.nord5,
				light2: nord.nord6, // light: background, dark: text

				error: nord.nord11,
			},
			fontFamily: {
				'logo': ['Pacifico']
			}
		}
	},
	plugins: [
		require('tailwind-nord'),
		require('@tailwindcss/forms'),
	]
};
