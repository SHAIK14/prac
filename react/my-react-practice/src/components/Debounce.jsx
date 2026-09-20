import {useState, useEffect} from 'react'
const Debounce =() =>{
  const [query, setQuery] = useState("")

  useEffect(()=>{
    const id = setTimeout(()=>{
      //run soem api or get api//
      console.log("query searched is:",query)
    },800)

    return ()=>(clearTimeout(id))
  },[query])


  return <>
    <input type="text" value={query} placeholder='serch the query' onChange={(e)=>setQuery(e.target.value)} />
  </>
}

export default Debounce
