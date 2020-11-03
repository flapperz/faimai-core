const express = require('express')

const app = express()
const port = 3000

const UUID = process.env.UUID

app.get('/', (req, res) => {
    res.send(`${UUID}`)
})
  
app.listen(port, () => {
    console.log(`listening at http://localhost:${port}`)
})