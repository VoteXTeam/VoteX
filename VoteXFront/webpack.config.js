const path = require("path");
const webpack = require("webpack");
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');

module.exports = {
    entry: [
        "./src/index.js"
    ],
    output: {
        path: path.resolve(__dirname, "./static/frontend"),
        filename: "main.js",
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                },
            },
        ],
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new BrowserSyncPlugin({
            host: 'localhost',
            port: 3000,
            proxy: 'http://127.0.0.1:8000',
            files: ['./src/**/*'],
        }),
        // new webpack.DefinePlugin({
        //     "process.env": {
        //         // This has effect on the react lib size
        //         NODE_ENV: JSON.stringify("production"),
        //     },
        // }),
    ],
};