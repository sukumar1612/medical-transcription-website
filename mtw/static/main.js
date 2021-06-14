const uploadForm = document.getElementById('upload-form')
const alertBox = document.getElementById('alert-box')
const progressBox = document.getElementById('progress-box')
const cancelBox = document.getElementById('cancel-box')
const cancelBtn = document.getElementById('cancel-btn')

async function handleform(event){
    event.preventDefault();

    progressBox.classList.remove('not-visible')
    cancelBox.classList.remove('not-visible')

    //form data
    const fd = new FormData(event.currentTarget);

    function sleep(delay) {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}
    //ajax
    $.ajax({
        type:'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: fd,
        beforeSend: function(){
            alertBox.innerHTML= ""
        },
        xhr: function(){
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', e=>{
                // console.log(e)
                if (e.lengthComputable) {
                    const percent = e.loaded / e.total * 100
                    console.log("percent completed :"+percent+"%")
                    progressBox.innerHTML = `<div class="progress">
                                                <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                            </div>
                                            <p>${percent.toFixed(1)}%</p>`
                }

            })
            cancelBtn.addEventListener('click', ()=>{
                xhr.abort()
                setTimeout(()=>{
                    uploadForm.reset()
                    progressBox.innerHTML=""
                    alertBox.innerHTML = ""
                    cancelBox.classList.add('not-visible')
                }, 2000)
            })
            return xhr
        },
        success: function(response){
            console.log(response)
            alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                    Successfully uploaded the file
                                </div>`
            cancelBox.classList.add('not-visible')
        },
        error: function(error){
            console.log(error)
            alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                    Ups... something went wrong
                                </div>`
        },
        cache: false,
        contentType: false,
        processData: false,
    })
}

const exampleForm = document.getElementById("upload-form");
exampleForm.addEventListener("submit", handleform);
