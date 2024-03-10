var btn;

window.addEventListener('load', function() {
    btn = document.getElementById("Summarize Video")
})

function execute() {
    btn.disabled = true;
    btn.innerHTML = "Summarizing...";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:5000/summary?url=https://www.youtube.com/watch?v=9fcOAo891Hs", true);
    xhr.onload = function() {
        var text = xhr.responseText;
        const p = document.getElementById("output");
        p.innerHTML = text;
        btn.disabled = false;
        btn.innerHTML = "Summarize";
    }
    xhr.send();

    // chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
    //     var url = tabs[0].url;
    //     var xhr = new XMLHttpRequest();
    //     xhr.open("GET", "http://127.0.0.1:5500/summary?url=" + url, true);
    //     xhr.onload = function() {
    //         var text = xhr.responseText;
    //         const p = document.getElementById("output");
    //         p.innerHTML = text;
    //         btn.disabled = false;
    //         btn.innerHTML = "Summarize";

    //     }
    //     xhr.send();
    // });
}

// btn.addEventListener("click", function() {
//     btn.disabled = true;
//     btn.innerHTML = "Summarizing...";
//     chrome.tabs.query({ currentWindow: true, active: true }, function(tabs) {
//         var url = tabs[0].url;
//         var xhr = new XMLHttpRequest();
//         xhr.open("GET", "http://127.0.0.1:3000/summary?url=" + url, true);
//         xhr.onload = function() {
//             var text = xhr.responseText;
//             const p = document.getElementById("output");
//             p.innerHTML = text;
//             btn.disabled = false;
//             btn.innerHTML = "Summarize";

//         }
//         xhr.send();
//     });
// });