const request = require('request');
const express = require("express") 
bodyParser = require('body-parser')
const path = require("path") 
const multer = require("multer") 
const app = express() 
var config = require("./config.json");

// View Engine Setup 
app.set("views",path.join(__dirname,"")) 
app.set("view engine","ejs") 
app.use(bodyParser.urlencoded({extended:true}));
app.use(bodyParser.json()); 
app.use( express.static( "Resources" ) );
// var upload = multer({ dest: "Upload_folder_name" }) 
// If you do not want to use diskStorage then uncomment it 
  
app.get("/",function(req,res){
    res.render("pages/index.ejs"); 
}) 
app.get("/clustering",function(req,res){ 
    
    res.render("pages/clustering.ejs", {config}); 
}) 
app.get("/data-upload",function(req,res){ 
    res.render("pages/data-upload.ejs");

}) 

// Port used for Node.JS will be port 8000 
app.listen(8000,function(error) { 
    if(error) throw error 
        console.log("Server created Successfully on PORT 8000") 
}) 