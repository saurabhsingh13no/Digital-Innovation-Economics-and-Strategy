module.exports=function(app){

    app.put("/api/search", search);

    var request=require('request');



    function search(req,res) {

        var obj = req.body;
        request.get('http://localhost:8080/users', function (error, response, body) {
            if(error){
                res.sendStatus(404);
            }
            else{

                res.send(body);
            }
        });





    }




};

