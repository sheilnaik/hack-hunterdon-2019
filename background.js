//background.js


function requestServer(myUrl){
	$.post( "http://ericjschneider.com:8080", myUrl, function( data ) {
  	$( ".result" ).html( data );
  	console.log( "Load was performed: " + data);
 	 myCallback(data);
	});

}


function myCallback(data){
	console.log("sending");
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		console.log("sending2");
  chrome.tabs.sendMessage(tabs[0].id, data, function(response) {
    console.log(response.farewell);
  });
});
}

// chrome.browserAction.OnClicked.addListener(function expandDiv(){
// 	chrome.runtime.sendMessage(function )
// })

chrome.tabs.onUpdated.addListener( function (tabId, changeInfo, tab) {
  console.log("changed, yo");
  chrome.tabs.query({
  active: true,
  currentWindow: true
}, function(tabs) {
  var tab = tabs[0];
  var url = tab.url;
    requestServer(url);
  console.log(url);

});
});
