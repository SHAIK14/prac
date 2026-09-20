import Warmup from "./components/Warmup"
import Pagination from "./components/Pagination"
import {Routes, Route, Link} from 'react-router-dom'

const App = ()=> {




  return (
    <>
      <nav>
        <Link to='/'>Home</Link>
        <Link to='/Warmup'>Warmup</Link>
        <Link to='/pagination'>Pagination</Link>

      </nav>
      <Routes>
        <Route path="/" element={<h1>react</h1>}></Route>
        <Route path="/Warmup" element={<Warmup/>}></Route>
        <Route path="/Pagination" element={<Pagination/>}></Route>

      </Routes>



    </>
  )
}

export default App
