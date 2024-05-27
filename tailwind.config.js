/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  darkMode: "media",
  theme: {
    fontFamily: {
      outfit: '"Outfit", sans-serif',
    },
    screens: {
      xxs: "320px",
      xs: "350px",
      sm: "640px",
      md: "768px",
      lg: "962px",
      xl: "1280px",
      "2xl": "1536px",
    },
    extend: {
       backgroundImage: {
        'banner-pattern': "url('/static/images/jajja-photo.jpg')",
      }
    },
  },
  plugins: [],
};
