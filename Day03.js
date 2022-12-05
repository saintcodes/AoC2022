const fs = require('fs')
  
fs.readFile('Day03data.txt', (err, data) => {
    if (err) throw err;
    let stringData = data.toString();
    console.log(stringData, "a;lskdfj")
  })