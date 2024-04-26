var updatebtns=document.getElementsByClassName('update-cart')


for(var i = 0; i<updatebtns.length; i++   ){
    updatebtns[i].addEventListener('click', function() {
        var productId=this.dataset.product
        var produkId=this.dataset.produk
        var action=this.dataset.action
        console.log('productId:', productId, 'action:',action)

        console.log('USER', user )
        if(user==='AnonymousUser'){
            console.log('Not logged in')
        }else{
            if (produkId){
                updateUserOrderp(produkId, action)
            }
            else{
                updateUserOrder(productId, action)
            }
        }
        
    })

}





function updateUserOrderp(produkId, action){
    console.log('User is logged in, sending data...')

    var url='/update_item/p'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':  csrftoken
        },
        body:JSON.stringify({'produkId': produkId, 'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data...')

    var url='/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':  csrftoken
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })
}
