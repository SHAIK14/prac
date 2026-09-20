import {useState} from 'react'

const ValidatedForm =()=>{
  const[data, setData] = useState({
    name:"",
    email:"",
    password: "",
  })
  const[dataTouched, setDataTouched] = useState({
    name:false,
    email:false,
    password: false,
  })

  const checkName = data.name.trim().length>0
  const checkMail = data.email.includes('@') && data.email.indexOf('.') > data.email.indexOf('@')
  const checkPassword = data.password.length >= 6

  const formvalid = checkName && checkMail && checkPassword



  const handleChange =(e)=>{
    const {name,value} = e.target
    setData(prev =>({...prev,[name]:value}))
  }
  const handleBlur =(e)=>{
    const {name} = e.target
    setDataTouched(prev =>({...prev,[name]:true}))
  }
  const handleSubmit =async (e) =>{
    e.preventDefault()
    console.log(data)

    const response = await fetch('--',{
      method:'POST',
      header:{},
      body:JSON.stringify(data)
    })

    const res = await response.json()
    console.log(res)



  }


  return <>

    <form onSubmit={handleChange}>
      <input
        type ='text'
        name='name'
        value={data.name}
        placeholder="enter the name"
        onChange={handleChange}
        onBlur ={handleBlur}
      />
      {!checkName && dataTouched.name &&<p>Name is required</p>}
      <input
        type ='text'
        name='email'
        value={data.email}
        placeholder="enter the email"
        onChange={handleChange}
        onBlur ={handleBlur}
      />
      {!checkMail && dataTouched.email &&<p>enter a valid email</p>}
      <input
        type ='text'
        name='password'
        value={data.password}
        placeholder="enter the password"
        onChange={handleChange}
        onBlur ={handleBlur}
      />
      {!checkPassword && dataTouched.password &&<p>enter a valid password</p>}

      <button type='submit' disabled={!formvalid} >submit</button>


    </form>

  </>
}

export default ValidatedForm
