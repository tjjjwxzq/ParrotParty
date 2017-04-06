var page = require('webpage').create(),
    host = "https://kopictf.herokuapp.com",
    // host = "https://127.0.0.1:5000",
    url = host+"/party-parrots",
    timeout = 20000,
    testIndex = 0,
    loadInProgress = false,
    form;

page.onNavigationRequested = function(url, type, willNavigate, main) {
  console.log("[URL] URL="+url);
};

page.onConsoleMessage = function(msg) {
  console.log(msg);
}

/********************************/

page.open(host, function (status) {
    page.evaluate(function() {
      document.getElementsByTagName("form")[0].elements["password"].value="ytraptorrap";
      $("button.btn")[0].click( function() {
        console.log("button clicked");
      });
    });

    setTimeout(function () {
        page.open(url, function (status) {
            setTimeout(function () {
                page.evaluate(function () {
                    console.log('haha');
                });
                phantom.exit();
            }, 5000);
        });
    }, 5000);
});
/********************************/

// console.log('??');
// page.open(host, function(status) {
//   console.log('opening page');
//   page.evaluate(function () {
//     $('body').load("https://kopictf.herokuapp.com/party-parrots", {_csrf_token: "avianparty",password: "ytraptorrap"}, function(status) {console.log(status)});
//   }
//   console.log(page.content);
//   phantom.exit();
// })

/**************** DIRECTLY OPENING /party-parrots ****************/
// var postBody = "_csrf_token=avianparty&password=ytraptorrap";
// console.log(JSON.stringify(postBody));

// page.open('http://kopictf.herokuapp.com/', function(status) {
//   console.log('status: ' + status);
//   page.evaluate(function () {
//         $('body').load("https://kopictf.herokuapp.com/party-parrots", {_csrf_token: "avianparty",password: "ytraptorrap"}, function(status) {console.log(status)});
//   })
//   // console.log(page.content);
//   phantom.exit();
// });

/********************************/

// page.open(url, function(status) {
//   console.log(page.content);
// })

// var csrf = '';

/********************************/
// page.open(host, function(status) {
//   console.log('opened page');
//   var csrf = page.evaluate(function () {
//     console.log('evaluating javascript');
//     document.getElementsByTagName("form")[0].elements["password"].value="ytraptorrap";
//     var _csrf = document.getElementsByTagName("form")[0].elements["_csrf_token"].value;
//     console.log(_csrf);
//     return _csrf;

//   });
//   var postBody = {_csrf_token: csrf, password: "ytraptorrap"};
//   console.log(JSON.stringify(postBody));
//   page.open(url, 'POST', postBody, function(status) {
//     console.log('status: ' + status);
//   });
//   phantom.exit();
// });

/**************** NAIVE NESTED PAGE.OPEN ****************/
// page.open(host, function(status) {
//   var script1 = 'function() { document.getElementsByTagName("form")[0].elements["password"].value="ytraptorrap"; document.getElementsByTagName("form")[0].submit(); }';
//   var script2 = 'function () { document.getElementsByTagName("form")[0].elements["password"].value="ytraptorrap"; $("button.btn")[0].click(function(){ $.post("/party-parrots", function(data) { return "success?"; }); }); }'
//   /* $("button.btn")[0].click(function(){        
//    *   $.post("/party-parrots", $("form")[0].serialize(), function(data) {
//    *       alert(data);
//    *   });
//    * });
//    */
//   // var script2 = 'function() { document.getElementsByTagName("form")[0].submit(); }';
//   // // console.log(page.evaluateJavaScript(script1););
//   // page.evaluateJavaScript(script2);
//   page.evaluateJavaScript
//   console.log("return: " + page.evaluateJavaScript(script2));
// 
//   console.log("Time to get exploited");
//   page.open(url, function() {
//     console.log(page.content);
//     var script3 = 'function() { document.querySelectorAll("html")[0].outerHTML; }';
//     page.evaluateJavaScript(script3);
//     console.log(script3);
//   })
//   console.log("[INFO] Phantom exit")
//   phantom.exit();  
// })

/**************** STEPS ****************/
// var steps = [
//   function() {
//     //Step 1: Load Login Page
//     page.open(host, function(status) {
//       console.log("[INFO] rendered page");
//       setTimeout(function(){
//         phantom.exit();
//       }, 1);
//     });
//   },
//   function() {
//     //Step 2: Enter Password
//     page.evaluate(function() {
//       console.log("[INFO] entering password");
      // form = document.getElementsByTagName("form")[0];
      // form.elements["password"].value="ytraptorrap";
//       console.log("Form: " + form);
//       return;

//     });
//   }, 
//   function() {
//     //Step 3: Submit Login Form
//     page.evaluate(function() {
//       form = document.getElementsByTagName("form")[0];
//       form.submit();
//       console.log("[INFO] submitted login form");
//       return;

//     });
//   }, 
//   function() {
//     // Output content of page to stdout after form has been submitted
//     page.evaluate(function() {
//       console.log(document.querySelectorAll('html')[0].outerHTML);
//     });
//   }
// ];


// interval = setInterval(function() {
//   if (!loadInProgress && typeof steps[testIndex] == "function") {
//     console.log("step " + (testIndex + 1));
//     console.log("Form: " + form);
//     steps[testIndex]();
//     testIndex++;
//   }
//   if (typeof steps[testIndex] != "function") {
//     console.log("test complete!");
//     phantom.exit();
//   }
// }, 50);