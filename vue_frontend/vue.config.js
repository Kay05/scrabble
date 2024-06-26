const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
        '/convert/': {
            target: 'http://127.0.0.1:8000',
            ws: true,
            changeOrigin: true
        }
    }
}
})
