#!/usr/bin/node
// Read from file

 const filesystem = require('fs');
 filesystem.readFile(process.argv[2], 'utf-8',
   function (error, data) {
     if (error) {
       console.log(error);
       return;
     }
     console.log(data);
   });
