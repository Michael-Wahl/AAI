<template>
  <div>
    <h2>Left: Preview Life Feed, Right: Image Captured</h2>
    <h3>Act out the following emotion: {{ prompts[currentPromptIndex] }}</h3>
    <h3> {{ result }}</h3>
    <video ref="video" width="640" height="480"></video>
    <canvas ref="canvas" width="640" height="480"></canvas>
    <br>
    <button @click="startSendingImages">Start Sending Images</button>
    <button @click="stopSendingImages">Stop Sending Images</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      interval: null,
      video: null,
      canvas: null,
      context: null,
      message: "",
      prompts: ['happy', 'sad', 'neutral', 'angry', 'disgust', 'fear'],
      currentPromptIndex: 0,
      result: "Emotion not recognized."
    };
  },
  mounted() {
    this.video = this.$refs.video;
    this.canvas = this.$refs.canvas;
    this.context = this.canvas.getContext("2d");

    // Get access to the webcam
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: false })
      .then(stream => {
        this.video.srcObject = stream;
        this.video.play();
      })
      .catch(err => {
        console.error("Error: ", err);
      });
  },
  methods: {
    startSendingImages() {
      // Start taking pictures every 1 second
      this.interval = setInterval(() => {
        this.context.drawImage(this.video, 0, 0, 640, 480);

        // Convert the canvas to a data URL and send to server using axios
        const imageData = this.canvas.toDataURL('image/png');
        axios.post('http://127.0.0.1:5000/image-upload', { image: imageData, target: this.prompts[this.currentPromptIndex] },
          { headers: { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' } })
          .then(response => {
            this.message = response.data
            console.log(this.message);
            if (this.message == 'Target matched') {
              this.result = 'Emotion recognized!'
              if (this.currentPromptIndex >= this.prompts.length - 1) {
                this.result = 'All emotions recorded. You are ready to play!'
                this.stopSendingImages();
              }
              else {
                this.currentPromptIndex++;
                this.result == 'Emotion not recognized.'
              }
            }
          })
          .catch(error => {
            console.error('Error sending image to server: ', error);
          });
      }, 1000);
    },
    stopSendingImages() {
      clearInterval(this.interval);
    }
  },
  beforeUnmount() {
    clearInterval(this.interval);
  },
};
</script>
