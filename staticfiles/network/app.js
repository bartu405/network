



function like(postId) {
    const likeButton = document.querySelector(`.like-button[data-post-id="${postId}"]`);
    const likesCount = document.getElementById(`number${postId}`);

    fetch('like', {
        method: 'POST',
        body: JSON.stringify({
            post_id: postId,
        }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.liked) {
                likeButton.textContent = 'Unlike';
            } else {
                likeButton.textContent = 'Like';
            }
            
            likesCount.textContent = data.likes_count;
        })
        .catch((error) => console.log(error));
}

document.querySelectorAll('.like-button').forEach((button) => {
    button.onclick = () => {
        const postId = button.dataset.postId;
        like(postId);
    };
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}








const edits = document.querySelectorAll('.edit')
const saves = document.querySelectorAll('.save')


for(let i = 0; i < edits.length ; i++) {
    let id = edits[i].dataset.id
    
    
    edits[i].addEventListener('click', () => {

        saves[i].style.display = 'block'

        edits[i].style.display = 'none'
        
        document.getElementById(`content${id}`).style.display = 'none'
        document.getElementById(`txt${id}`).style.display = 'block'

        
       

            
    
    })
    
}

for(let i = 0; i < saves.length ; i++) {
    let id = saves[i].dataset.id

    let user_id = saves[i].dataset.user_id
    
    

    saves[i].addEventListener('click', () => {
        edits[i].style.display = 'block'
        saves[i].style.display = 'none'
        document.getElementById(`content${id}`).style.display = 'block'
        document.getElementById(`txt${id}`).style.display = 'none'



        let bro = document.getElementById(`txt${id}`).value
        
        document.getElementById(`content${id}`).innerHTML = bro 

        fetch('edit', {
            method: 'POST',
            body: JSON.stringify({
                "user_id": user_id, 
                "id": id,
                "body": bro
            })
        })
        .then(response => response.json )
        .then()
        .catch(error => console.log(error));

    })
    
    
}



