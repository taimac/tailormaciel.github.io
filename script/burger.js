const buger= document.getElementById('burger');
const navMenu=document.getElementById('menu');
const cross=document.getElementById('cross');


buger.addEventListener('click', ()=> {
    navMenu.classList.remove('remove');
    navMenu.classList.toggle('show')
})

cross.addEventListener('click', ()=> {
    navMenu.classList.toggle('remove');
    navMenu.classList.remove('show');
    
})

navMenu.addEventListener('click', ()=> {
    navMenu.classList.remove('show');
})
