// const data = {
//   title: "xxxx",
//   author: "xxxx",
//   publication_date: "2023-05-01",
//   price: 10.00
// }

// fetch('http://localhost:8000/books/create/',{
//     method:'POST',
//     headers:{
//       "Content-type":"application/json"
//     },
//     body: JSON.stringify(data)
//   })
//   .then(res=>res.json())
//   .then(data=>{
//     console.log(data);
//   })
//   .catch(e => {
//     console.log(e);
//   })

fetch('http://localhost:8000/books/all/',{
  method:'GET'
})
.then(res=>res.json())
.then(data=>{
  console.log(data);
})
.catch(e => {
  console.log(e);
})