/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

const colors = require("tailwindcss/colors");

module.exports = {
  content: [
    "!./node_modules/**/*",
    "!**/*/node_modules/**/*",
    "../../templates/**/*.html",
    "../../static/images/dashboard_svg.svg",
    "../../**/*.js",
    "../../**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#D49E8D",
        currentColor: "#D49E8D",
        cyan: colors.cyan,
        "dark-goldenrod": "#B08401",
        "tan": "#D49E8D",
        "dust-storm": "#DED1BD",
        "white-smoke": "#FAF6F2",
        "van-dyke-brown": "#683B2B"
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
