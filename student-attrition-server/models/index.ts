import fs from 'fs';

export function init(){
  /** Initialises all models in the database for use by the server. */
  fs.readdirSync(__dirname).forEach(function(file){
    if(file !== 'index.js' && file !== 'index.ts'){
      const fileName = file.split('.')[0];
      const model = require('./' + fileName)
      module.exports[model.modelName] = model
    }
  })
}