/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./404.html",
    "./pages/**/*.{html,js}",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class', // Habilita o dark mode baseado em classe
  theme: {
    extend: {
      colors: {
        'amarelo-principal': '#FFD700',
        'amarelo-secundario': '#f59e0b',
      }
    },
  },
  plugins: [],
}