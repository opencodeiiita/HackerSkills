


const inputs=document.querySelectorAll('input');

const patterns={
password:/^[\w@-]{8,20}$/,
email:/^([a-z\d\.-]+)@gmail.com$/
};



function validate(field,regex){
   if(regex.test(field.value))
   {
     field.className='valid';
   }else{
     field.className='invalid';
   }
}

inputs.forEach((input) => {
 input.addEventListener('keyup',(e) =>
{

  validate(e.target,patterns[e.target.attributes.name.value])

   });
});
