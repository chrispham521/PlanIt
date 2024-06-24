const express= require('express');
const app = express();
const path=require('path');
const session = require('express-session');
const bodyParser = require('body-parser');
const passport = require('passport');
const connectEnsureLogin = require('connect-ensure-login');

const User = require('./Back-End/user');

const connectDB = require('./Back-End/database_connection');
port=3000 || process.env.port;


app.engine('html', require('ejs').renderFile);


connectDB();
app.use(express.json({extended: false}));


// app.use('/api/userModel',require('./Back-End/userAPI'));

/*app.get('/planner', (req, res) => {
    console.log(__dirname)
    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python3', ['monthly_planner.py']);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        dataToSend = "data:application/pdf;base64," + dataToSend;
        // window.open(pdfAsDataUri);
        res.send(dataToSend)
    });
});*/

const {PDFDocument, StandardFonts, rgb }=require('pdf-lib');
const fs = require('fs')
async function  runfunction(){
    const content= await PDFDocument.load(fs.readFileSync('./Front-End/planner.pdf'));

}
runfunction().catch((err) => console.log(err))



app.use("/",express.static(path.join(__dirname, 'Front-End')));

app.listen(port, () => {
    console.log('Application listening on port 3000!');
});
app.get('/', (req, res) => {
    res.sendFile(`${__dirname}/Front-End/index.html`);
});


app.use(session({
    secret: 'r8q,+&1LM3)CD*zAGpx1xm{NeQhc;#',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60 * 60 * 1000 } // 1 hour
}));

// Configure More Middleware
app.use(bodyParser.json());  
app.use(bodyParser.urlencoded({ extended: false }));

app.use(passport.initialize());
app.use(passport.session());


// // Passport Local Strategy
passport.use(User.createStrategy());

// passport.use(new LocalStrategy(User.authenticate('local')));

// // To use with sessions
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());



app.post('/signup', async(req,res)=>{

    const{username, password} = req.body;
    const user = new User({username})
    const registeredUser = await User.register(user,password)
    // res.send(registeredUser)
    res.redirect('/login');
    // res.sendFile(__dirname + '/Front-End/login.html');

})

app.post('/login', passport.authenticate('local', { failureRedirect: '/failedAuth' }),  async(req, res)=>{
    // res.send('hi')
    req.session._id = req.user._id;
	const foundUser = await User.findById(req.session._id);
    // res.sendFile(__dirname + '/Front-End/secret.html');
    // res.send(foundUser)
    // res.sendFile(__dirname + '/Front-End/secret.html');
    // console.log('hi')
    res.redirect('/secret');
    // res.redirect('/secret');
    // res.render(__dirname + '/Front-End/index.html');
});

// app.post('/login',  async(req, res)=>{
    // const {username,password} = req.body
    // res.send(password)
// });

// app.post('/login', async(req,res)=>{
//     res.send('hi')
// })

app.get('/testlogin', async(req,res)=>{
    if (req.session._id){
        res.send('u are logged in.')
    }
    else{
        res.send('u are not logged in.')
    }
})

app.get('/secret', connectEnsureLogin.ensureLoggedIn(), async(req, res) => {
    res.sendFile(__dirname + '/Front-End/secret.html');
});

app.get('/dashboard', connectEnsureLogin.ensureLoggedIn(), async(req, res) => {
    // res.send('hi')
    res.send(`Hello ${req.user.username}. Your session ID is ${req.sessionID}   
    and your session expires in ${req.session.cookie.maxAge} 
    milliseconds.<br><br>
    <a href="/logout">Log Out</a><br><br>
    <a href="/secret">Members Only</a>`);
});

app.get('/logout', async(req, res)=>{
    req.logout();
    // res.sendFile(__dirname + '/Front-End/login.html');

    res.redirect('/login');
});

app.get('/failedAuth', async(req,res)=>{
    res.sendFile(__dirname + '/Front-End/login.html');
});

app.get('/login', async(req, res) => {
    res.sendFile(__dirname + '/Front-End/login.html');
  });

app.get('/signup', async(req, res) => {
    res.sendFile(__dirname + '/Front-End/signup.html');
  });