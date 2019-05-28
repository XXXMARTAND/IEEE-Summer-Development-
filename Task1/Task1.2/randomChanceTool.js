import 'dotenv/config';
import cors from 'cors';
import express from 'express';

const app = express();

var randomChanceTool = [];

//Generating a random value from randomChanceTool
app.get('/randomChanceTool', (req, res) => {
	var i = Math.floor(Math.random()*randomChanceTool.length);
	return res.send({Value:`${randomChanceTool[i]}`});
});

//Adding sample space to randomChanceTool
app.post('/randomChanceTool', (req, res)=>{
	var curLength = randomChanceTool.length;
	randomChanceTool.push(curLength+1);
	return res.send({message:`Added one sample space. Total now: ${randomChanceTool[curLength]}`});
});

//Deleting sample space from randomChanceTool
app.delete('/randomChanceTool', (req, res) => {
	randomChanceTool.pop();
	var curLength = randomChanceTool.length;
	return res.send({message:`Deleted one sample space. Total now: ${randomChanceTool[curLength]}`});

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
