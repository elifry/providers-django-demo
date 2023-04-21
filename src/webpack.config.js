const path = require("path");

module.exports = {
  entry: {
    index: "./assets/index.js", // path to our input file
    slides: "./assets/slides/slides.js",
  },
  output: {
    filename: "[name]-bundle.js", // output bundle file name
    path: path.resolve(__dirname, "./static"), // path to our Django static directory
  },
  stats: {
    errorDetails: true,
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
};
