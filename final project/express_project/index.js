const express = require('express');
const users = require("./users");

const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://meni1547:mg138462@cluster0.wbaet34.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";



const app = express();
const port = 3001;
// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);

app.use("/users", users);

app.get('/', (req, res) => {
  res.send('Hello World!')
})
app.post('/', (req, res) => {
    res.send('Got a POST request')
  })

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})