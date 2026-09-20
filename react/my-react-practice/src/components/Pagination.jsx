import {useState, useEffect} from'react'
const items =[
  { id: 1,  name: "Item 1" },
  { id: 2,  name: "Item 2" },
  { id: 3,  name: "Item 3" },
  { id: 4,  name: "Item 4" },
  { id: 5,  name: "Item 5" },
  { id: 6,  name: "Item 6" },
  { id: 7,  name: "Item 7" },
  { id: 8,  name: "Item 8" },
  { id: 9,  name: "Item 9" },
  { id: 10, name: "Item 10" },
  { id: 11, name: "Item 11" },
  { id: 12, name: "Item 12" },
  { id: 13, name: "Item 13" },
  { id: 14, name: "Item 14" },
  { id: 15, name: "Item 15" },
  { id: 16, name: "Item 16" },
  { id: 17, name: "Item 17" },
  { id: 18, name: "Item 18" },
  { id: 19, name: "Item 19" },
  { id: 20, name: "Item 20" },
  { id: 21, name: "Item 21" },
  { id: 22, name: "Item 22" },
  { id: 23, name: "Item 23" }
]

const fetchitems = (page,limit)=>{
  return new Promise((resolve) =>{
    setTimeout(() =>{
      const start = (page-1)*limit
      const end = page * limit
      resolve({
        data : items.slice(start,end),
        totalpages: Math.ceil(items.length/limit)
      })
    },800)

  })
}

const Pagination =()=>{
  const[page,setPage] = useState(1)
  const[data,setData] = useState([])
  const [totalPages, setTotalPages] = useState(1);
  const[loading,setLoading] = useState(false)
  const limit = 5

  useEffect(()=>{
    setLoading(true)
    fetchitems(page,limit).then((res)=>{
      setData(res.data)
      setTotalPages(res.totalpages)
      setLoading(false)
    })



  },[page])




  return <>
    <h1> pagination</h1>
    <div>
      { loading? <p>Loading....</p> :
      <ul>
        {data.map(item =>{
          return <li key = {item.id}>{item.name}</li>
        })}
      </ul>
      }
    </div>

    <div>
      <button disabled ={page ===1} onClick={()=>setPage(prev => prev-1)}>prev</button>
      page{page} of {totalPages}
      <button disabled ={page >=totalPages } onClick={()=>setPage(prev => prev+1)}>next</button>
    </div>

  </>
}

export  default Pagination
