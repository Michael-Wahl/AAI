<!-- html goes between the template-tags, everything has to be sourrounded by one div-element -->
<template>
    <div>
        <img crossorigin="anonymous" :src="imageSrc[currentImage].path">
        <br />
        <!-- @-symbol to call methods defined below in script section -->
        <button @click="checkAnswer('happy')">Happy</button>
        <button @click="checkAnswer('sad')">Sad</button>
        <button @click="nextImage" :disabled="IsNextDisabled">Next Image</button>
        <!-- variables can be accessed between the {{}} -->
        <p>Your Anwer is {{ result }}</p>
        <br />
        <!-- <input type="file" name="newFile" @change="addNewImage($event)" /> -->

    </div>
</template>


<!-- javascript section -->
<script>

// import will be needed later for connecting to the backend
//import axios from 'axios'

export default {
    data() {
        // all variables have to be declared in this list
        return {
            result: "Not clicked yet",
            currentImage: 0,
            imageSrc: [
                {path : 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Aurora_in_Abisko_near_Tornetr%C3%A4sk.jpg/640px-Aurora_in_Abisko_near_Tornetr%C3%A4sk.jpg'},
                {path : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Berlin_Opera_UdL_asv2018-05.jpg/600px-Berlin_Opera_UdL_asv2018-05.jpg'}
            ],
            IsNextDisabled: false,
            newFile: null,
            message: ""
        }
    },
    //methods have to be defined in this list
    methods: {
        checkAnswer(value) {
            if (value == "happy") {
                this.result = "Correct!"
            }
            else {
                this.result = "Incorrect!"
            }
        },
        nextImage() {
            if (this.currentImage < this.imageSrc.length - 1) {
                this.currentImage += 1
            }
            else {
                this.IsNextDisabled = true
            }

        },
        // for uploading pictures to the backend
        /* addNewImage(event) {
            console.log(event.target.files[0])
            this.newFile = event.target.files[0]
            let formData = new FormData();
            formData.append('file', this.newFile)

            axios.post('http://127.0.0.1:5000/', formData).then(response => {
                this.message = response.data.message;
                console.log(this.message)
                this.imageSrc.push({path: 'http://127.0.0.1:5000/uploads/' + this.newFile.name})
                this.IsNextDisabled = false

            });
        } */
    }

};
</script>
