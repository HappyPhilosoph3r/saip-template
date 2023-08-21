export function alphaSortObject(obj: any){
  const keys = Object.keys(obj)
  keys.forEach(key => {
    const values = obj[key]
    if(values instanceof Array){
      values.sort((a, b) => {
        const lowerCaseA = a.toLowerCase()
        const lowerCaseB = b.toLowerCase()
        return lowerCaseA > lowerCaseB ? 1 : lowerCaseA < lowerCaseB ? -1 : 0
      })
      obj[key] = values
    }
  })
  return obj
}