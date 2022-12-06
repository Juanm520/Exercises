function deepFreeze(obj) {
for (item in obj)
  if(typeof obj[item] === 'object')
     deepFreeze(Object.freeze(obj[item]))   
 return Object.freeze(obj)
}

