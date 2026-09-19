import ProfileCard from './components/Profilecard'
import {useState} from 'react'
const App = ()=> {

  const [show, setShow] = useState(false)
  const[count, setCount] = useState(0)




  const fruits =["mangoes","apples","bananas"]


  return (
    <>
      <ProfileCard name="asif" role="fullstack" />
      <div>
        <ul>
        {fruits.map((fruit,idx) =>{
          return <li key={idx}>{fruit}</li>
        })}
      </ul>
      </div>
      <div>
        {show?"grind 2days":""}
        <button onClick={()=>setShow((prev)=>!prev)}>showme</button>
      </div>
      <div>
        <button onClick={()=>setCount((prev)=> prev+1)}> + </button> {count} <button onClick={()=>setCount((prev)=> prev-1)}> - </button>
      </div
    </>
  )
}

export default App
