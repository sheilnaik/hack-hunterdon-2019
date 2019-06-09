//content.js

var current_url = window.location.href
console.log(current_url)
// $.post(url, {"url": current_url}, function(data){
// 	console.log(data);
// });

//injection of our warning badge into divs
function showBadge() {
var suggest = document.createTextNode("Consider these alternate, less problematic products");
var dealDiv = document.getElementById("unifiedPrice_feature_div")
var btn  = document.createElement("BUTTON");
var t = document.createTextNode("You have blocked this company!");
var div = document.createElement("div");
div.style.height = "0px";
div.id = "dropdown";
div.innerHTML = 
div.style.overflow = "hidden";
div.style.background = "white";
div.style.align = "center";
var isVisible = false;


if (dealDiv !== null){
	btn.appendChild(t);
	dealDiv.appendChild(btn);
	dealDiv.appendChild(div);
	btn.addEventListener('click', function cb(event) {
    // ...one-time handling of the click event...
    if (isVisible === false){
    	div.style.overflow = "visible";
    	div.style.height = "50px";
    	document.getElementById("unifiedPrice_feature_div").appendChild(div);
    	isVisible = true;
    } else{
    	div.style.height = "0px";
    	div.style.overflow = "hidden";
    	isVisible = false;
    }
    
});
}



//there's another div
var featureDiv = document.getElementById("superleafPitchPrice_feature_div");
if (featureDiv !== null){
	btn.appendChild(t);
	featureDiv.appendChild(btn);
	featureDiv.appendChild(div);
	btn.addEventListener('click', function cb(event) {
	  // ...one-time handling of the click event...
	 if (isVisible === false){
    	div.style.overflow = "visible";
    	div.style.height = "50px";
    	document.getElementById("unifiedPrice_feature_div").appendChild(div);
    	isVisible = true;
    } else {
    	div.style.height = "0px";
    	div.style.overflow = "hidden";
    	isVisible = false;
    }
});
}
}

var badgeShown = false;

chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse){
		console.log("getting: " + request);
        if (request === "True" && badgeShown === false){
            showBadge();
            badgeShown = true;
        }
  //       jay = JSON.parse(request);
  //       //working off read                                                   ;
		// document.getElementById("dropdown").innerHTML = "<a href="+jay["one"][0]+">"+jay["one"][1]+"</a>" + "<br>"
  //           +"<a href="+jay["two"][0]+">"+jay["two"][1]+"</a>"+"<br>" + "<a href="+jay["three"][0]+">"+jay["three"][1]+"</a>";
        //hardcoded for show
        document.getElementById("dropdown").innerHTML = "<a href=https://google.com>Folgers</a>" + "<br>" +
            "<a href=https://google.com>Blue Mountain</a>" + "<br>" +"<a href=https://www.amazon.com/Lavazza-4202A-Pound-Super-Espresso/dp/B0002E2FH0/ref=sxin_2_ac_d_rm?keywords=coffee+beans&pd_rd_i=B0002E2FH0&pd_rd_r=ddce6405-5c80-4a18-807d-b847c29f406a&pd_rd_w=HsKAl&pd_rd_wg=sp43V&pf_rd_p=91b604bb-c371-4573-970f-bed68a552852&pf_rd_r=H8BARCBNXGGPYJHHFWNP&qid=1560082248&s=gateway>Lavazza</a>" + "<br>";
        sendResponse({farewell:"goodbye"});
	}
);

//document.getElementById("dropdown").innerHTML = 
