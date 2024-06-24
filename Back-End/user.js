const mongoose = require('mongoose');
const express = require('express');
const passportLocalMongoose = require('passport-local-mongoose');

const route = express.Router();

const UserSchema = new mongoose.Schema({
    username:{
        type:String
    },

})

UserSchema.plugin(passportLocalMongoose);

const User = mongoose.model('user', UserSchema);
module.exports = User;

