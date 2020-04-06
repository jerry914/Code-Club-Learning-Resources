var bg;
var img;
var bgcolor = [];
function preload() {
    img = loadImage(getValue());

}
function setup() { 
    bg = selectAll('.content');
    
    // for(var i=0;i<img.width;i++){
    //     for(var j=0;j<img.height;i++){
    //         console.log("d");
    //     }
    // }
    bg.style('background-color', img.get(10,10));
} 

function draw() { 
}

function getValue(){

    var url = window.location.href;
    var qparts = url.split("?");
    if (qparts.length == 0){return "";}
    var query = qparts[1];
    var vars = query.split("=");
    var value = vars[1];
    vars = value.split("&");
    return vars[0];
}