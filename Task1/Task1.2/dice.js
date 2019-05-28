import 'dotenv/config';
import cors from 'cors';
import express from 'express';

const app = express();

let dice = [1,2,3,4,5,6];

//Generating a random value from dice
app.get('/dice', (req, res) => {
	var i = Math.floor(Math.random()*dice.length) ;
	return res.send({Value: `${dice[i]}`});
})

//Adding sample space to dice. Which results in error
app.post('/dice', (req, res) => {
	res.status(500).send({error:"Cannot add sample space to a dice."});
});

//Deleting sample space from dice. Which results in an error
app.delete('/dice', (req, res) => {
	res.status(500).send({error:"Can't delete sample space from a dice"});
});

//404 messages for any other address than previously defined
app.get('*', (req,res)=>{
	res.status(404).send({error:"404"});
});

app.post('*', (req,res)=>{
	res.status(404).send({error:"404"});
});

app.delete('*', (req,res)=>{
	res.status(404).send({error:"404"});
});

//listening on PORT
app.listen(process.env.PORT, () => 
	console.log(`Listening on port ${process.env.PORT}`),
);
