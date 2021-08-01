addEventListener('DOMcontentloaded',() => {
    const boton = document.querySelector ('#boron')

        const obtener_pixeles = () => document.documentElement.scrollTop || document.body.scrollTop
        const irarriba = () => {
            if (obtener_pixeles() > 0){


                scrollTo(0,0)
            }
        } 
        boton.addEventListener('click', irarriba)
})