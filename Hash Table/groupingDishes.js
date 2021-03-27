function groupingDishes(dishes) {
    let hash = {}
    
    dishes.forEach((dish)=>{
        let name = dish[0]
        
        for(let i=1; i<dish.length; i++){
            if(!hash[dish[i]]){
                hash[dish[i]]=[]
                hash[dish[i]].push(name)
            }else{
                hash[dish[i]].push(name)
            }
        }
    })
    
    
    return select(hash)
    
}


function select(hash){
    let selected = []
    
    
    
    for(const [k,v] of Object.entries(hash)){

        if(v.length>1){
            let arr = []
            arr.push(k)
            arr = arr.concat(v.sort())
            selected.push(arr)
        }
    }
    
    
    return selected.sort((a, b) => a[0] < b[0] ? -1 : a[0] === b[0] ? 0 : 1)
}