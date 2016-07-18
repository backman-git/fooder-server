var express         =       require("express");
var multer          =       require('multer');
var app             =       express();
var sys = require('sys')
var exec = require('child_process').exec;
var fname ="";
var fs = require("fs");
var bodyParser = require('body-parser');




function puts(error, stdout, stderr) { sys.puts(stdout) }




// server behavior


//1. upload new restaurant ,restaurant => RS
var newRS_route='/fooder/newRS'
var RSDB_path='./fooder/main/DB/imgRS'
var addRS_filePath='.\\script\\addRS.bat'


var newRS_ID=0;
var uploadForRS      =   multer({ dest: RSDB_path, rename: function(fieldname, filename) {
	UpImgName= 'R'+newRS_ID;
	newRS_ID+=1;
	
return UpImgName;}});



app.get(newRS_route,function(req,res){
      res.sendFile(__dirname + "/newRestaurant.html");
	 
});




app.post(newRS_route,uploadForRS,function(req,res){
	
		// maybe add some secret
		console.log('- process upload restaurant.');
      
    
        if ( Object.keys(req.files).length === 0 ){
            var meg="- no restaurant is uploaded"
			
			console.log(meg);
			res.json({status:'noFile'});
			
		
		}
		else{
			
			console.log("longitude "+req.body.longitude)
			console.log("latitude "+req.body.latitude)
			console.log('-process this image of restaurant.');
			
		
		//image process
			// add mutiple process 
			//insert database  UpImgName is ID
			console.log('- insert database ');
			var gValue=0,bValue=0;	
			exec(addRS_filePath+" "+UpImgName+" "+req.body.longitude+" "+req.body.latitude+" "+gValue+" "+bValue,function (error, stdout, stderr) { 
				
				res.send(stdout);
			
			
			});
			
			
	
			
		}
	
});

//2. upload new fooder , fooder => FD
var newFD_route='/fooder/newFD'
var FDDB_path='./fooder/main/DB/imgFD'
var addFD_filePath='.\\script\\addFD.bat'
var newFD_ID=0;
var uploadForFD      =   multer({ dest: FDDB_path, rename: function(fieldname, filename) {
	UpImgName= 'F'+newFD_ID;
	newFD_ID+=1;
	
return UpImgName;}});



//Upload new fooder 
app.get(newFD_route,function(req,res){
      res.sendFile(__dirname + "/newFooder.html");
});

//should find one method of naming

app.post(newFD_route,uploadForFD,function(req,res){
	
		// maybe add some secret
		console.log('- process upload fooder.');
      
    
        if ( Object.keys(req.files).length === 0 ){
            var meg="- no fooder is uploaded"
			
			console.log(meg);
			res.json({status:'noFile'});
			
		
		}
		else{
			
			
			console.log('- execute the new fooder.');
			// add mutiple process 
			
			//insert database &extract feature  UpImgName is ID
			console.log('- insert database & extract features.');
			var gValue=0;
			var bValue=0;
			
			exec(addFD_filePath+" "+req.body.RSID+" "+UpImgName+" "+gValue+" "+bValue,function (error, stdout, stderr) { 
			
				res.send(stdout);
			
			
			});
			
			
	
			
		}
	
});




//analysis RS


var analysisRS_route = '/fooder/analysisRS'
var queryPool ='./fooder/main/RS/queryPool'
var answerPool='./fooder/main/RS/answerPool'
var analysisRS_filePath= '.\\script\\analysisRS.bat'

app.get(analysisRS_route,function(req,res){
      res.sendFile(__dirname + "/analysisRS.html");
	  	  
});

var waitID=0;
var AsFileName="";
var uploadForAnalysis     =   multer({ dest: queryPool, rename: function(fieldname, filename) {
	AsFileName= waitID;
	
return AsFileName;}});

// maybe change upload image to upload feature!

app.post(analysisRS_route,uploadForAnalysis,function(req,res){
    
		console.log('- analysis uploaded RS ID: '+AsFileName);
		
        if ( Object.keys(req.files).length === 0 ) {
            console.log('no files uploaded');
			res.send("{\"status\":\"noFile\"}");
			
		}
		else if(typeof req.body.latitude=='undefined' || typeof req.body.longitude=="undefined"){
			res.send("{\"status\":\"noLocation\"}");

		}
		else{
			console.log("-execute analysis process");
			
			//multiple process
			exec("rm "+answerPool+"/"+waitID+".json")
			//gps & image
			// maybe change upload image to upload feature!
	
			exec(analysisRS_filePath+" "+waitID+" "+req.body.longitude+" "+req.body.latitude,puts);
		
			fs.writeFile(answerPool+"/"+waitID+".json", "{\"status\":\"processing\"}", function(err) {
				if(err) {
					return console.log(err);
				}

			
				console.log("-upload for analysis successful!");
				res.json({status:"success", ID:waitID});
			}); 
		
			
			
			
			
		}	
		waitID+=1;
		
	
	
});
var answerRS_route='/fooder/resultRS'
var answerPath='/fooder/main/RS/answerPool'
app.get(answerRS_route,function(req,res){
    
	var ID= req.param('ID')	
	if(ID!= null && ID<100){
		
		res.sendFile(__dirname +answerPath+'/'+ID+".json");
		
	}
	else
		res.send("give me ID");
	
});


//analysis FD

var analysisFD_route = '/fooder/analysisFD'
var queryPoolFD ='./fooder/main/FD/queryPool'
var answerPoolFD='./fooder/main/FD/answerPool'
var analysisFD_filePath= '.\\script\\analysisFD.bat'

app.get(analysisFD_route,function(req,res){
      res.sendFile(__dirname + "/analysisFD.html");
	  	  
});

var waitID=0;
var AsFileName="";
var uploadForAnalysis     =   multer({ dest: queryPoolFD, rename: function(fieldname, filename) {
	AsFileName= waitID;
	
return AsFileName;}});

// maybe change upload image to upload feature!

app.post(analysisFD_route,uploadForAnalysis,function(req,res){
    
		console.log('- analysis uploaded FD ID: '+AsFileName);
		
        if ( Object.keys(req.files).length === 0 ) {
            console.log('no files uploaded');
			res.send("{\"status\":\"noFile\"}");
			
		}
		else{
			console.log("-execute analysis process");
			
			//multiple process
			exec("rm "+answerPoolFD+"/"+waitID+".json")
			//gps & image
			// maybe change upload image to upload feature!
	
			exec(analysisFD_filePath+" "+waitID+" "+req.body.RSID,puts);
		
			fs.writeFile(answerPoolFD+"/"+waitID+".json", "{\"status\":\"processing\"}", function(err) {
				if(err) {
					return console.log(err);
				}

			
				console.log("-upload for analysis successful!");
			}); 
		
			
			
			
			res.json({status:"success", ID:waitID});
		}	
		waitID+=1;
		
	
	
});
var answerFD_route='/fooder/resultFD'
var answerPathFD='/fooder/main/FD/answerPool'
app.get(answerFD_route,function(req,res){
    
	var ID= req.param('ID')	
	if(ID!= null && ID<100){
		
		res.sendFile(__dirname +answerPathFD+'/'+ID+".json");
		
	}
	else
		res.send("give me ID");
	
});






//voting!

var votingFD_route='/fooder/voting'
var votingFD_filePath ='.\\script\\votingFD.bat'
app.get(votingFD_route,function(req,res){
    
	 res.sendFile(__dirname + "/voting.html");
	
	
});



var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.post(votingFD_route,urlencodedParser,function(req,res){
    
		
		
		
		if(req.body.ID && req.body.votingType){
			exec(votingFD_filePath+" "+req.body.ID+" "+req.body.RSID+" "+req.body.votingType,function(error, stdout, stderr){
				
				
				res.send(stdout);
				
				
				
				
			});
			
			
			
			
			
			
		}
		else{
			
			
			res.json({status:"unsuccess"});
			
		}
		
		
	
	
	
});







app.listen(300,function(){
    console.log("Working on port 300");
});