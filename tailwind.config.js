/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./themes/riskitera/layouts/**/*.html", "./content/**/*.md"],
  theme: {
    extend: {
      colors: {
        rk: {
          'bg': '#0b1220',
          'card': '#111827',
          'card-hover': '#1a2332',
          'border': '#1e2d3d',
          'text': '#e6eaf2',
          'text-secondary': '#8892a4',
          'blue': '#3b82f6',
          'violet': '#8b5cf6',
          'cyan': '#06b6d4',
        }
      },
      fontFamily: {
        sans: ['ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
