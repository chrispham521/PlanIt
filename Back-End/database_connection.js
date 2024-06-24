const mongoose = require('mongoose');
const URI = 'mongodb+srv://Plannit:Plannit123@cluster-plannit.vu6v8.mongodb.net/PlannitDB?retryWrites=true&w=majority';

const connectDB = async()=>{
    await mongoose.connect(URI,{
        useUnifiedTopology: true,
        useNewUrlParser: true
    });
    console.log('Database has been connected...!');
}

module.exports = connectDB;