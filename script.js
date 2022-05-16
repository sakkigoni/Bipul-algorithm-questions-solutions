function download(filesize) {
    var content = [];
    memory = (filesize * 1024 * 1024) / 8;
    var element = document.createElement("a");
    var ans_hex = 0;
    for (var i = 0; i < memory; i++) {
      ans = Math.floor(Math.random() * (1000000 - 1) + 1);
      ans_hex = parseInt(ans, 10).toString(16);
      ans_hex = ans_hex.padStart(8, "0");
      content.push(ans_hex);
    }
  
    element.setAttribute(
      "href",
      "data:text/plain;charset=utf-8," + encodeURIComponent(content.join(""))
    );
    element.setAttribute("download", "file.txt");
    element.style.display = "none";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  }
  