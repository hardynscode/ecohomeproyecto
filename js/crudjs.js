  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional

    
    
    const openModal = document.getElementById("openRegisterModel")
    
    const modal = document.getElementById("modal")
    
    const closeModal = document.getElementById('closeRegisterModel')
    
    const registerform = document.getElementById('register-form')
    
    
    
    const showRegisterModal = () => {
        modal.classList.toggle('is-active')
    }
    
    openModal.addEventListener('click', showRegisterModal)
    closeModal.addEventListener('click', showRegisterModal)
    registerform.addEventListener("submit", (e) => {

        e.preventDefault()

        const nombre = registerform["nombre"].value
        console.log(nombre)

    })
    
    
    