<template>
    <div>
        <button @click="getImageList(); getEmotions()">Start Game</button>
        <br>
        <button @click="prevImage">Previous</button>
        <FaceCrop :imageUrl = "imageUrl" :coordinates = "currentFaceCoords" :staticImageUrl = "staticImageUrl"/>
        <button @click="nextImage">Next</button>
        <br>
        <button @click="checkAnswer('neutral')">Neutral</button>
        <button @click="checkAnswer('happy')">Happy</button>
        <button @click="checkAnswer('sad')">Sad</button>
        <button @click="checkAnswer('angry')">Angry</button>
        <button @click="checkAnswer('disgust')">Disgust</button>
        <button @click="checkAnswer('fear')">Fear</button>
        <p>Your Anwer is {{ guessResult }} !</p>

    </div>
</template>
  
<script>
import axios from 'axios';
import FaceCrop from './FaceCrop.vue'

export default {
    components: {
        FaceCrop
    },
    data() {
        return {
            imageUrl: '',
            imageList: [],
            currentImageIndex: 0,
            emotions: {},
            filename: '',
            emotion: '',
            guessResult: '',
            currentFaceCoords: [88, 250, 100, 200],
            staticImageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Royal_Wedding_Stockholm_2010-Slottsbacken-05_edit.jpg/640px-Royal_Wedding_Stockholm_2010-Slottsbacken-05_edit.jpg",
        }
    },
    mounted() {
        this.getEmotions()
        this.getImageList()
    },
    methods: {
        // Getting list of all classified images on the server
        async getImageList() {
            try {
                const response = await axios.get('http://localhost:5000/getAllImages')
                this.imageList = response.data
                this.getImage(this.imageList[this.currentImageIndex])
                this.getEmotion(this.imageList[this.currentImageIndex])
            } catch (error) {
                console.log(error)
            }
        },
        // Getting list of all emotions results for all classified images
        async getEmotions() {
            try {
                const response = await axios.get('http://localhost:5000/getAllEmotions')
                this.emotions = response.data
                console.log(this.emotions)
            }
            catch (error){
                console.log(error)
            }
        },
        async getEmotion(imageName) {
            try{
                const response = await axios.get(`http://localhost:5000/getEmotion/${imageName}`)
                const xmax = response.data[0].xmax
                const xmin = response.data[0].xmin
                const ymax = response.data[0].ymax
                const ymin = response.data[0].ymin
                this.currentFaceCoords = [xmin, ymin, xmax, ymax]
                console.log(this.currentFaceCoords)
            }
            catch (error){
                console.log(error)
            }
        },
        // Getting image file for specific image
        async getImage(imageName) {
            try {
                const response = await axios.get(`http://localhost:5000/getImage/${imageName}`, {

                    headers: {
                        'content-type': 'image/png',
                        'accept': 'image/png'
                    },
                    responseType: 'blob'
                })
                this.imageUrl = window.URL.createObjectURL(new Blob([response.data]))
            } catch (error) {
                console.log(error)
            }
        },
        prevImage() {
            this.guessResult = ''
            this.currentImageIndex--
            if (this.currentImageIndex < 0) {
                this.currentImageIndex = this.imageList.length - 1
            }
            this.getImage(this.imageList[this.currentImageIndex])
            this.getEmotion(this.imageList[this.currentImageIndex])
        },
        nextImage() {
            this.guessResult = ''
            this.currentImageIndex++
            if (this.currentImageIndex >= this.imageList.length) {
                this.currentImageIndex = 0
            }
            this.getImage(this.imageList[this.currentImageIndex])
            this.getEmotion(this.imageList[this.currentImageIndex])
        },
        // For current image, lookup what the emotion should be and adjust the anwer text
        checkAnswer(value) {
            this.filename = this.imageList[this.currentImageIndex]
            this.emotion = this.emotions[this.filename]
            console.log(this.emotion[0].emo_label)
            if (value == this.emotion[0].emo_label) {
                this.guessResult = 'Correct'
                console.log('CORRECT')
            }
            else {
                this.guessResult = 'Incorrect'
                console.log('INCORRECT')
            }
        },
    }
}
</script>
  